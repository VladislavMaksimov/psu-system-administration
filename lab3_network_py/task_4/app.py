import subprocess
import socket
from threading import Thread

def ping(ip):
    cmd = "ping -n 1 " + ip
    response = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in response.stdout.readlines():
        line = line.strip()
        if line:
            # print(line.decode('cp866'))
            if bytes('TTL', 'cp866') in line:
                print(f'{ip} имеет публичный доступ.')
                return
    # print('\n\n')

ip = socket.gethostbyname(socket.getfqdn())
ip_parced = ip.split('.')
ip = '.'.join([ip_parced[0], ip_parced[1], ip_parced[2]])

for host in range(1, 255):
    host_ip = '.'.join([ip,str(host)])
    # ping(host_ip)
    Thread(target=ping, args=[host_ip]).start()