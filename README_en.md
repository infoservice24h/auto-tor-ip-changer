# 🧅 Auto Tor IP Changer

🔄 **Protect your privacy by automatically rotating your IP using the Tor network.**

Automate changing your public IP at scheduled intervals through Tor as a proxy.  
Ideal for anonymous browsing, ethical scraping, automated testing, and enhanced personal privacy.

## 🚀 Why Use This?

- **Dynamic Privacy**: Periodically change your network identity.
- **Simple Automation**: Quick installation and straightforward configuration.
- **Open Source**: Full transparency and the ability to customize.
- **Compatibility**: Works on various Linux distributions and Termux.

## 📦 Installation

Clone the repository and run the installer:

```bash
git clone https://github.com/infoservice24h/auto-tor-ip-changer.git
cd auto-tor-ip-changer
chmod +x src/install.sh
sudo ./src/install.sh
```

## ⚙️ Configuration

Config file: `/etc/auto_tor_ip_changer/config.conf`

Example:
```ini
[TOR]
intervalo = 30

[API]
verificar_ip = true
api_url = https://api.ipify.org
```

Customize as needed and restart the service:
```bash
sudo systemctl restart auto_tor_ip.service
```

## 📝 Usage

- Check service status:
  ```bash
  sudo systemctl status auto_tor_ip.service
  ```
- View logs in real-time:
  ```bash
  tail -f /var/log/auto_tor_ip.log
  ```

## 🌐 Documentation via GitHub Pages

https://infoservice24h.github.io/auto-tor-ip-changer/

## 🤝 Contributions

Contributions are welcome! Open issues and PRs for improvements, fixes, or new ideas.

## 📄 License

MIT License
