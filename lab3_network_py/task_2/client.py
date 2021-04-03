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

while True:
    cmd = input('> ').strip()

    if cmd == 'exit':
        connector.close()
        sys.exit()

    connector.sendall(bytes(cmd, 'utf8'))

    data = connector.recv(1024).decode()
    print(data)