#!/usr/bin/env python3
import os, time, requests, configparser
from stem import Signal
from stem.control import Controller

CONFIG_FILE = '/etc/auto_tor_ip_changer/config.conf'
LOG_FILE = '/var/log/auto_tor_ip.log'

def log(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

def get_ip(api):
    try: return requests.get(api).text.strip()
    except Exception as e: log(f"Erro IP: {e}"); return None

def renew():
    try:
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)
    except Exception as e:
        log(f"Erro renovar: {e}")

def main():
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE)
    wait = int(cfg['TOR'].get('intervalo', 30))
    check = cfg['API'].getboolean('verificar_ip', True)
    api = cfg['API'].get('api_url', 'https://api.ipify.org')
    while True:
        renew()
        if check:
            ip = get_ip(api)
            if ip: log(f"Novo IP: {ip}")
        time.sleep(wait)

if __name__ == "__main__":
    main()
