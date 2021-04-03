import subprocess
import socket
from threading import Thread

def ping(ip):
    cmd = "ping -n 1 " + ip
    response = subprocess.run(cmd, capture_output=True)
    if bytes('TTL', 'cp866') in response.stdout:
        print(f'{ip} имеет публичный доступ.')

ip = socket.gethostbyname(socket.getfqdn())
ip_parced = ip.split('.')
ip = '.'.join([ip_parced[0], ip_parced[1], ip_parced[2]])

for host in range(1, 255):
    host_ip = '.'.join([ip,str(host)])
    Thread(target=ping, args=[host_ip]).start()