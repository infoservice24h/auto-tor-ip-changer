#!/bin/bash
set -e
apt update && apt install -y tor python3 python3-pip
pip3 install stem requests
cp src/usr/local/bin/auto_tor_ip_changer.py /usr/local/bin/
chmod +x /usr/local/bin/auto_tor_ip_changer.py
mkdir -p /etc/auto_tor_ip_changer
cp src/etc/auto_tor_ip_changer/config.conf /etc/auto_tor_ip_changer/
cp src/etc/systemd/system/auto_tor_ip.service /etc/systemd/system/
systemctl daemon-reexec || true
systemctl daemon-reload
systemctl enable auto_tor_ip.service
systemctl start auto_tor_ip.service
