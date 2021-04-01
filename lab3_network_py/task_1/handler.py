from socketserver import BaseRequestHandler

class FileHandler(BaseRequestHandler):
    methods = ['auth', 'list', 'info', 'retr', 'help']

    def help(self):
        help_str = "auth user pass — авторизация, user и pass хранятся в файле pass в каталоге запуска программы\nlist — показать список файлов в каталоге запуска программы\ninfo file — напечатать сведения о файле, mime тип, размер, время создания\nretr file1 file2 file_n — передать файлы, указанные в строке\nexit — выход\nhelp — справка по командам"
        self.request.sendall(bytes(help_str, 'utf8'))

    def handle(self):
        while True:
            data = self.request.recv(1024).decode()

            cmd = data.split()
            if len(cmd) == 0:
                continue

            method, *args = cmd
            if method not in self.methods:
                continue

            if method == 'help':
                self.help()