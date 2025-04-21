from PIL import ImageFont
import serial
import time
import subprocess
import os
from macros import macros

# === Konfigurace ===
PORT = "/dev/tty.usbmodem3101"
BAUD = 115200
ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)
print("🔌 Connected to ESP32-C3")

# === Stavy ===
STATE_SELECT = 0
STATE_ACTIVE = 1
current_state = STATE_SELECT
selected_screen = 0

# Dynamické názvy obrazovek podle macros
screen_names = [screen["name"] for screen in macros.values()]

# Barvy režimů
screen_colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
]


def center_text(line: str, width_chars=21):
    line = line.strip()
    spaces = max((width_chars - len(line)) // 2, 0)
    return " " * spaces + line


def send_framebuffer(lines):
    ser.write(b"DISPLAY_FRAME_BEGIN\n")
    for i, line in enumerate(lines):
        centered_line = center_text(line)
        ser.write(f"DISPLAY_LINE:{i}:{centered_line}\n".encode())
    ser.write(b"DISPLAY_FRAME_END\n")
    print("→ Sent framebuffer")


def update_display():
    if current_state == STATE_SELECT:
        lines = ["Select mode:"]
        for i, name in enumerate(screen_names):
            prefix = ">" if i == selected_screen else " "
            lines.append(f"{prefix} {i + 1}. {name}")
        send_framebuffer(lines)
    else:
        macros_for_screen = macros[selected_screen]["keys"]
        layout = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"]]

        lines = ["Active mode:"]

        for idx, row in enumerate(layout):
            cols = []
            for key in row:
                shortcut = macros_for_screen.get(key, {}).get("icon", key)
                shortcut = shortcut.strip().upper()[:3].ljust(3)
                cols.append(shortcut)
            lines.append(" | ".join(cols))
            if idx < len(layout) - 1:
                lines.append(
                    "---------------------"
                )  # Přidá prázdný řádek pouze mezi řádky

        send_framebuffer(lines)


def update_led():
    r, g, b = screen_colors[selected_screen % len(screen_colors)]
    ser.write(f"LED_ALL:{r}:{g}:{b}\n".encode())


def render_macro_grid(screen_index):
    keys = macros.get(screen_index, {}).get("keys", {})
    layout = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["A", "B", "C"]]

    lines = []
    for row in layout:
        line = ""
        for idx, key in enumerate(row):
            label = keys.get(key, {}).get("icon", "").ljust(3)[:3].upper()
            line += f"{label}"
            if idx < len(row) - 1:
                line += " │ "
        lines.append(line)
        lines.append("───────────────")  # podtržítko pod každým řádkem

    return lines


# === Inicializace ===
update_display()
update_led()

# === Smyčka ===
while True:
    line = ser.readline().decode().strip()
    if not line:
        continue

    print("←", line)

    if line == "ENC_LEFT":
        if current_state == STATE_SELECT:
            selected_screen = (selected_screen - 1) % len(screen_names)
            update_display()
            update_led()

    elif line == "ENC_RIGHT":
        if current_state == STATE_SELECT:
            selected_screen = (selected_screen + 1) % len(screen_names)
            update_display()
            update_led()

    elif line == "ENC_PRESS":
        current_state = STATE_ACTIVE if current_state == STATE_SELECT else STATE_SELECT
        update_display()
        update_led()

    elif line.startswith("KEY_") and current_state == STATE_ACTIVE:
        key = line[4:]
        current_macros = macros.get(selected_screen, {}).get("keys", {})
        macro = current_macros.get(key)

        if macro:
            label = macro.get("label", "No macro")
            shortcut = macro.get("shortcut", key)
            # send_framebuffer([shortcut, "", label])
        else:
            send_framebuffer([f"No macro for key {key}"])

        if macro and "color" in macro:
            r, g, b = macro["color"]
            ser.write(f"LED_ALL:{r}:{g}:{b}\n".encode())

            cmd = macro.get("command")
            if cmd:
                if "{{CWD}}" in cmd:
                    project_path = os.getcwd()
                    cmd = cmd.replace("{{CWD}}", project_path)
                subprocess.Popen(cmd, shell=True)
        else:
            ser.write(b"LED_ALL:50:50:50\n")
