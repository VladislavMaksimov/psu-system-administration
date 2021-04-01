import socket
import sys

# берёт ip из аргумента командной строки
if len(sys.argv) == 2:
    try:
        ip = socket.gethostbyname(sys.argv[1]) 
    except socket.gaierror:
        print("Ошибка: неправильный хост.")
        sys.exit()
else:
    print("Введите IP")
    sys.exit()

print("Сканирую: " + ip)
print()

try:
    for port in range(1,65535):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.5)
        try:
            connect = scanner.connect((ip,port))
            print('Порт {} открыт'.format(port))
            connect.close()
        except:
            pass
except KeyboardInterrupt:
        print("Программа завершена пользователем.")
        sys.exit()
except socket.error:
        print("Сервер не отвечает.")
        sys.exit()