macros = {
    0: {
        'name': 'System',
        'keys': {
            '1': {'label': 'Lock Screen', 'color': (200, 0, 0), 'command': 'pmset displaysleepnow', 'icon': 'Lock', 'shortcut': 'LCK'},
            '2': {'label': 'Play/Pause', 'color': (0, 200, 0), 'command': 'osascript -e "tell application \\"System Events\\" to key code 16"', 'icon': 'Play', 'shortcut': 'PL>'},
            '3': {'label': 'Toggle Mute', 'color': (150, 0, 150), 'command': 'osascript -e "set volume output muted not (output muted of (get volume settings))"', 'icon': 'Mute', 'shortcut': 'MT!'},
            '4': {'label': 'Volume Down', 'color': (255, 140, 0), 'command': 'osascript -e "set volume output volume ((output volume of (get volume settings)) - 10)"', 'icon': 'Vol-', 'shortcut': 'V-'},
            '5': {'label': 'Volume Up', 'color': (255, 165, 0), 'command': 'osascript -e "set volume output volume ((output volume of (get volume settings)) + 10)"', 'icon': 'Vol+', 'shortcut': 'V+'},
            '6': {'label': 'Open Downloads', 'color': (0, 100, 255), 'command': 'open ~/Downloads', 'icon': 'Dwnld', 'shortcut': 'DL>'},
            '7': {'label': 'Empty Trash', 'color': (255, 0, 50), 'command': 'osascript -e "tell application \\"Finder\\" to empty trash"', 'icon': 'Trash', 'shortcut': 'TRS'},
            '8': {'label': 'Spotify', 'color': (0, 150, 150), 'command': 'open -a "Spotify"', 'icon': 'Spoty', 'shortcut': 'SPF'},
            '9': {'label': 'Mission Control', 'color': (100, 100, 255), 'command': 'osascript -e "tell application \\"System Events\\" to key code 160"', 'icon': 'Missn', 'shortcut': 'MC'},
            'A': {'label': 'Screenshot', 'color': (0, 100, 200), 'command': 'screencapture -c', 'icon': 'Shot', 'shortcut': 'SCR'},
            'B': {'label': 'Do Not Disturb', 'color': (50, 50, 100), 'command': 'shortcuts run "Do Not Disturb"', 'icon': 'DND', 'shortcut': 'DND'},
            'C': {'label': 'Sleep Mac', 'color': (0, 0, 100), 'command': 'pmset sleepnow', 'icon': 'Sleep', 'shortcut': 'ZZZ'}
        }
    },
    1: {
        'name': 'Productivity',
        'keys': {
            '1': {'label': 'Clockify Open', 'color': (0, 100, 255), 'command': 'open -a "Clockify Desktop"', 'icon': 'Clkfy', 'shortcut': 'CLK'},
            '2': {'label': 'Clockify Play/Pause', 'color': (255, 165, 0), 'command': '''osascript -e 'tell application "Clockify Desktop" to activate' -e 'tell application "System Events" to keystroke "r" using {command down}' ''', 'icon': 'C>||', 'shortcut': 'C>'},
            '3': {'label': 'Clockify Stop', 'color': (255, 0, 0), 'command': '''osascript -e 'tell application "Clockify Desktop" to activate' -e 'tell application "System Events" to keystroke "e" using {command down, shift down}' ''', 'icon': 'CStop', 'shortcut': 'C×'},
            'A': {'label': 'Open Clockify', 'color': (0, 100, 255), 'command': 'open -a "Clockify"', 'icon': 'Clkfy', 'shortcut': 'OPN'},
            '4': {'label': 'Cirque Gmail', 'color': (0, 255, 150), 'command': 'open -na "Google Chrome" --args --profile-directory="Profile 1" https://mail.google.com', 'icon': 'MailC', 'shortcut': 'ML1'},
            '5': {'label': 'Chat Gmail', 'color': (255, 255, 0), 'command': 'open -na "Google Chrome" --args --profile-directory="Profile 1" "https://mail.google.com/mail/u/0/#chat/home"', 'icon': 'Chat', 'shortcut': 'CHT'},
            '6': {'label': 'Personal Mail', 'color': (100, 255, 100), 'command': 'open -na "Google Chrome" --args --profile-directory="Default" https://mail.google.com', 'icon': 'MailP', 'shortcut': 'PM1'},
            '7': {'label': 'Reminders', 'color': (255, 80, 80), 'command': 'open -a "Reminders"', 'icon': 'Remnd', 'shortcut': 'RMD'},
            '8': {'label': 'Open Notion', 'color': (80, 100, 255), 'command': 'open -a "Notion"', 'icon': 'Notion', 'shortcut': 'NTN'},
            '9': {'label': 'Start Pomodoro', 'color': (255, 100, 0), 'command': 'shortcuts run "Start Pomodoro"', 'icon': 'Pmdro', 'shortcut': 'PMD'},
            'B': {'label': 'Break Timer', 'color': (0, 180, 255), 'command': 'shortcuts run "Start Break Timer"', 'icon': 'Break', 'shortcut': 'BRK'},
            'C': {'label': 'Break + Lock', 'color': (200, 0, 0), 'command': 'pmset displaysleepnow', 'icon': 'BLock', 'shortcut': 'BLK'}
        }
    },
    2: {
        'name': 'Finder & Code',
        'keys': {
            '1': {
                'label': 'Open Developer Folder',
                'color': (0, 150, 255),
                'command': '''
osascript -e 'tell application "Finder"
    activate
    open POSIX file "/Users/jakubpatera/Developer"
end tell'
&& sleep 1
&& osascript -e 'tell application "System Events" to key code 125'
''',
                'icon': 'DevFld',
                'shortcut': 'DEV'
            },
            '2': {
                'label': 'Open in VS Code',
                'color': (0, 200, 255),
                'command': '''
osascript -e 'tell application "System Events" to keystroke "o" using {command down}'
sleep 0.5
osascript -e '
tell application "Finder"
    try
        set thePath to POSIX path of (folder of the front window as alias)
        do shell script "open -a \\"Visual Studio Code\\" " & quoted form of thePath
    on error
        return
    end try
end tell
'
''',
                'icon': 'VSCode',
                'shortcut': 'COD'
            },
            "3": {
              "label": "Format Code",
              "icon": "FMT",
              "color": (0, 200, 200),
              "command": 'osascript -e \'tell application "System Events" to keystroke "f" using {option down, shift down}\''

            },
            'A': {'label': 'Sleep', 'color': (0, 0, 100), 'command': 'pmset sleepnow', 'icon': 'Sleep', 'shortcut': 'Z.Z'},
            "4": {
               "label": "Open Terminal",
            "icon": "TRM",
            "color": (0, 255, 150),
            "command": 'osascript -e \'tell application "System Events" to keystroke "`" using {control down}\''
            },
            "5": {
                "label": "Run react app",
            "icon": ">RA",
            "color": (255, 100, 100),
            "command": 'osascript -e \'tell application "System Events" to keystroke "npm run dev" & return\''
            },

        }
    },
    3: {
        'name': 'Power',
        'keys': {
            '1': {'label': 'Shutdown', 'color': (255, 0, 0), 'command': 'osascript -e "tell application \\"System Events\\" to shut down"', 'icon': 'Shutd', 'shortcut': 'OFF'},
            '2': {'label': 'Restart', 'color': (255, 100, 0), 'command': 'osascript -e "tell application \\"System Events\\" to restart"', 'icon': 'Rstrt', 'shortcut': 'RST'},
            'A': {'label': 'Sleep', 'color': (0, 0, 100), 'command': 'pmset sleepnow', 'icon': 'Sleep', 'shortcut': 'Z##'}
        }
    },


}


