# 🧅 Auto Tor IP Changer

🔄 **Proteja sua privacidade trocando seu IP automaticamente com a rede Tor.**

Automatize a troca do seu IP público em intervalos programados usando Tor como proxy.  
Ideal para navegação anônima, raspagem ética, testes automatizados e reforço de privacidade pessoal.

## 🚀 Por que usar?

- **Privacidade Dinâmica**: Mude sua identidade de rede periodicamente.
- **Automação Simples**: Instalação rápida e configuração intuitiva.
- **Código Aberto**: Transparência total e possibilidade de customização.
- **Compatibilidade**: Funciona em diversas distribuições Linux e Termux.

## 📦 Instalação

Clone e execute o script de instalação:

```bash
git clone https://github.com/infoservice24h/auto-tor-ip-changer.git
cd auto-tor-ip-changer
chmod +x src/install.sh
sudo ./src/install.sh
```

## ⚙️ Configuração

Arquivo: `/etc/auto_tor_ip_changer/config.conf`

```ini
[TOR]
intervalo = 30

[API]
verificar_ip = true
api_url = https://api.ipify.org
```

Personalize conforme necessidade e reinicie o serviço:
```bash
sudo systemctl restart auto_tor_ip.service
```

## 📝 Uso

- Verificar status do serviço:
  ```bash
  sudo systemctl status auto_tor_ip.service
  ```
- Visualizar logs em tempo real:
  ```bash
  tail -f /var/log/auto_tor_ip.log
  ```

## 🌐 Documentação via GitHub Pages

https://infoservice24h.github.io/auto-tor-ip-changer/

## 📘 English

Veja o README em inglês: [README_en.md](README_en.md)

## 🤝 Contribuições

Contribuições são bem-vindas! Abra issues e PRs para melhorias, correções ou novas ideias.

## 📄 Licença

MIT License
