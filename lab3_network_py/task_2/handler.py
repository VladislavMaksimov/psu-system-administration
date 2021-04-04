from socketserver import BaseRequestHandler
import os

class FileHandler(BaseRequestHandler):
    methods = ['auth', 'list', 'read', 'send', 'help']
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    authorized = False
    user = None

    def send_err(self, err):
        self.request.sendall(bytes(err, 'utf8'))

    def send_succ(self, succ):
        self.request.sendall(bytes(succ, 'utf8'))

    def help(self):
        help_str = (
        "auth user pass — авторизация, user и pass хранятся в файле pass в каталоге запуска программы\n"
        "list — показать список сообщений. Собщения храняться в каталоге\n"
        "messages/username, где username это имя пользователя системы (из auth).\n"
        "Сообщения характеризуются номером и темой.\n"
        "read msg — вывести сообщение под номером msg\n"
        "send user — ввод сообщения для пользователя. Запрашиватеся тема, ввод заканчивается одиночным символом «.»\n"
        "exit — выход\n"
        "help — справка по командам."
        )
        self.request.sendall(bytes(help_str, 'utf8'))

    def auth(self, user, pas):
        if self.authorized == True:
            return True
        f = open(os.path.join(self.__location__, 'pass'))
        correct_user, correct_pas = f.readlines()
        if user.strip() == correct_user.strip() and pas.strip() == correct_pas.strip():
            self.user = user
            return True
        else:
            return False

    def get_messages(self):
        path = '\\'.join([self.__location__, self.user])
        directory = os.listdir(path)
        files = [ f for f in directory if os.path.isfile('\\'.join([path,f]))]
        messages = [ f for f in files if f.endswith(".msg") ]
        return messages

    def list(self):
        messages = self.get_messages()
        messages_str = ' '.join(messages)
        if len(messages) > 0:
            self.request.sendall(bytes(messages_str, 'utf8'))
        else:
            self.request.sendall(bytes('Сообщений нет.', 'utf8'))

    def read_msg(self, message):
        path = '\\'.join([self.__location__, self.user, message])
        f = open(path)
        content = f.readlines()
        self.request.sendall(bytes(''.join(content), 'utf8'))


    def read(self, msg):
        messages = self.get_messages()
        for message in messages:
            num, theme = message.split(' ')
            if int(num) == int(msg):
                self.read_msg(message)
                return
        self.send_err('Нет темы с таким номером.')

    def send(self, user, num, theme, message):
        path = '\\'.join([self.__location__, user])
        msg_file = ' '.join([num, theme]) + '.msg'
        msg_path = '\\'.join([path, msg_file])
        f = open(msg_path, 'w')
        f.write(message)
        self.send_succ('Сообщение отправлено.')



    # определяет поведение сервера
    def handle(self):
        while True:
            data = self.request.recv(1024).decode()

            cmd = data.split()
            if len(cmd) == 0:
                continue

            method, *args = cmd
            if method not in self.methods:
                self.send_err('Такого метода нет!')
                continue

            if method == 'help':
                self.help()
                continue

            if method == 'auth':
                try:
                    self.authorized = self.auth(*args)
                    if not self.authorized:
                        self.send_err('Неправильное сочетание логина и пароля!')
                    else:
                        self.send_succ('Вы авторизованы.')
                except TypeError:
                    self.send_err('Введите логин и пароль!')
                except Exception as e:
                    print(e)
                finally:
                    continue
            elif not self.authorized:
                self.send_err('Необходимо авторизоваться!')
                continue

            if method == 'list':
                self.list()
                continue

            if method == 'read':
                try:
                    self.read(*args)
                except TypeError:
                    self.send_err('Введите номер сообщения.')
                except:
                    self.send_err('Введите корректный номер сообщения.')
                finally:
                    continue

            if method == 'send':
                self.send(*args)