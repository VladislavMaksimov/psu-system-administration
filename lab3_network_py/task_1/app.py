import os
from sys import exit
from mimetypes import guess_type
import time
import datetime

methods = ['auth', 'list', 'info', 'retr', 'help', 'exit']
authorized = False
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

print('Здравствуйте! Введите help, чтобы узнать команды.')

def help():
    print('auth user pass — авторизация, user и pass хранятся в файле pass в каталоге запуска программы\n'
          'list — показать список файлов в каталоге запуска программы\n'
          'info file — напечатать сведения о файле, mime тип, размер, время создания\n'
          'retr file1 file2 file_n — передать файлы, указанные в строке\n'
          'exit — выход\nhelp — справка по командам')

def auth(user, pas):
    if authorized == True:
        return True
    f = open(os.path.join(__location__, 'pass'))
    correct_user, correct_pas = f.readlines()
    if user.strip() == correct_user.strip() and pas.strip() == correct_pas.strip():
        return True
    else:
        return False

def list():
    directory = os.listdir('.')
    files = ' '.join(filter(os.path.isfile, directory))
    print(files)

def info(file):
    if os.path.isfile(file):
        mime = guess_type(file)[0]
        size = os.path.getsize(file)
        ctime = os.path.getctime(file)
        pretty_ctime = datetime.datetime.fromtimestamp(ctime).strftime('%Y-%m-%dT%H:%M:%S')
        info = 'MIME: {}\n'.format(mime) + 'Размер: {}\n'.format(size) + 'Время создания: {}'.format(pretty_ctime)
        print(info)
    else:
        print('Это не файл.')

def retr(files):
    for f in files:
        fname = os.path.basename(f)
        path = os.path.abspath(f)
        new_path = __location__ + '\\hell'
        try:
            os.mkdir(new_path)
        except FileExistsError:
            pass
        os.rename(path, new_path + '\\' + fname)

while True:
    cmd = input('> ').strip().split(' ')
    method, *args = cmd

    if method not in methods:
        print('Команда ' + method + ' не распознана.')
        continue
    
    if method == 'exit':
        exit()

    if method == 'help':
        help()
        continue
    
    if method == 'auth':
        try:
            authorized = auth(*args)
            if not authorized:
                print('Неправильное сочетание логина и пароля!')
            else:
                print('Вы авторизованы.')
        except TypeError:
            print('Введите логин и пароль!')
        finally:
            continue
    elif not authorized:
        print('Необходимо авторизоваться!')
        continue
    
    if method == 'list':
        list()
        continue

    if method == 'info':
        try:
            info(args[0])
        except IndexError:
            print('Введите название файла.')
        finally:
            continue
    
    if method == 'retr':
        retr(args)