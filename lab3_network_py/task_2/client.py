import socket
import sys

# ввод хоста и порта из командной строки
if len(sys.argv) == 3:
    try:
        host = socket.gethostbyname(sys.argv[1])
        port = int(sys.argv[2])
    except socket.gaierror:
        print("Ошибка: неправильный хост.")
        sys.exit()
else:
    print("Введите хост и порт.")
    sys.exit()

connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connector.connect((host, port))
except socket.error:
    print('Сервер не отвечает.')
    sys.exit()

def get_theme():
    while True:
        print('Введите тему сообщения.')
        theme = input('> ').strip()
        if theme == '':
            continue
        else:
            return theme

def get_message():
    while True:
        print('Введите сообщение.')
        message = input('> ').strip()
        if message == '':
            continue
        else:
            return message

def send(cmd):
    theme = get_theme()
    message = get_message()

    method, user = cmd.split(' ')
    num_cmd = ' '.join(['num', user])
    connector.sendall(bytes(num_cmd, 'utf8'))
    num = connector.recv(1024).decode()

    new_cmd = ' '.join([cmd, num, theme, message])
    return new_cmd
    
while True:
    cmd = input('> ').strip()

    if cmd == 'exit':
        connector.close()
        sys.exit()

    if 'send' in cmd:
        cmd = send(cmd)

    connector.sendall(bytes(cmd, 'utf8'))

    data = connector.recv(1024).decode()
    print(data)