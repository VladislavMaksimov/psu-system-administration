import subprocess
import socket
from graphviz import Digraph
from concurrent.futures import ThreadPoolExecutor

def get_length(response):
    resp_units = response.decode('cp866').split(' ')
    for unit in resp_units:
        if 'время' in unit:
            u = unit.split('=')
            return int(u[1].strip('мс'))

def ping(ip, root_ip):
    global dot
    cmd = "ping -n 1 " + ip
    response = subprocess.run(cmd, capture_output=True)
    if bytes('TTL', 'cp866') in response.stdout:
        dot.node(ip, ip)
        length = get_length(response.stdout)
        dot.edge(root_ip, ip, minlen=str(length))

dot = Digraph(format='png')
ip = socket.gethostbyname(socket.getfqdn())
dot.node(ip, ip)
ip_parced = ip.split('.')
new_ip = '.'.join([ip_parced[0], ip_parced[1], ip_parced[2]])

with ThreadPoolExecutor(max_workers=255) as executor:
    for host in range(1, 255):
        host_ip = '.'.join([new_ip,str(host)])
        if host_ip != ip:
            executor.submit(ping, host_ip, ip)


print(dot.source)
dot.render('test.gv', view=True)