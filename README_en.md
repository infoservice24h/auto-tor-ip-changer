
# 🧅 Auto Tor IP Changer

Automatically rotate your public IP using the Tor network. Ideal for privacy, penetration testing, scraping and OSINT. Runs as a background service on Linux systems.

## 🚀 Features
- Automatic IP change using Tor (NEWNYM signal)
- Configurable interval (default: 30 seconds)
- Optional external IP check
- Logs to /var/log with timestamp and IP
- One-line installation script (install.sh)
- systemd service support

## 🛠️ Installation
```bash
git clone https://github.com/infoservice24h/auto-tor-ip-changer.git
cd auto-tor-ip-changer
chmod +x src/install.sh
sudo ./src/install.sh
```
