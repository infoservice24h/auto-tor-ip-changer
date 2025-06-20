# 🧅 Auto Tor IP Changer

> Troque seu endereço IP público automaticamente via rede Tor com um único comando.

![Tor Logo](https://upload.wikimedia.org/wikipedia/commons/3/38/Tor-logo-2011-flat.svg)

---

## 🚀 Sobre o Projeto

O **Auto Tor IP Changer** é uma ferramenta de linha de comando que utiliza a rede Tor para trocar seu IP de forma programada, segura e anônima. Ideal para:

- Privacidade avançada
- Testes de rede (pentest)
- Automação com IP rotativo
- Contornar restrições geográficas

---

## ⚙️ Instalação

No Termux, Linux ou ambiente Unix-like:

```bash
git clone https://github.com/infoservice24h/auto-tor-ip-changer.git
cd auto-tor-ip-changer
chmod +x src/install.sh
sudo ./src/install.sh
```

> 📝 Requer Python 3 e Tor instalados

---

## 🧪 Uso

Execute o script diretamente:

```bash
python3 /usr/local/bin/auto_tor_ip_changer.py
```

> Seu IP será trocado a cada execução.

---

## 🔧 Funcionalidades

✅ Alternância automática de IP pela rede Tor  
✅ Detecção e exibição do novo IP público  
✅ Agendamento com cron suportado  
✅ Código aberto e auditável  
✅ Ideal para Termux, VPS e Linux Desktop

---

## 📷 Exemplo de Saída

```bash
[INFO] IP antigo: 88.12.43.1
[INFO] Novo IP Tor: 185.220.101.54
```

---

## 🌐 GitHub Pages

Para ver a apresentação visual do projeto:  
📄 https://infoservice24h.github.io/auto-tor-ip-changer/

---

## 🛡️ Licença

Distribuído sob a licença MIT.  
Desenvolvido por [iNFO SERVICE 24h](https://github.com/infoservice24h) 🧠
