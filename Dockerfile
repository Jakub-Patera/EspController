FROM python:3.10-slim

# Instalace OS nástrojů pro osascript a Chrome
RUN apt-get update && apt-get install -y \
    libdbus-glib-1-2 \
    dbus \
    && rm -rf /var/lib/apt/lists/*

# Kopírování kódu
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .

# Defaultní příkaz
CMD ["python", "main.py"]
