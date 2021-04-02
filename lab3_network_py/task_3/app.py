import os
from sys import exit
from math import sqrt

methods = ['login', 'store', 'solve', 'exit']
authorized = False
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
A = None
B = None
C = None

def login(user, pas):
    global authorized
    if authorized == True:
        return 0
    f = open(os.path.join(__location__, 'pass'))
    correct_user, correct_pas = f.readlines()
    if user.strip() == correct_user.strip() and pas.strip() == correct_pas.strip():
        authorized = True
        return 0
    else:
        return 1

def store(a, b, c):
    global A
    global B
    global C
    A, B, C = int(a), int(b), int(c)
    return 0

def solve(a=None, b=None, c=None):
    if a is not None and b is not None and c is not None:
        a = int(a)
        b = int(b)
        c = int(c)
    elif a is None and b is None and c is None:
        a, b, c = A, B, C
    else:
        raise TypeError
    D = b*b - 4*a*c
    x1 = None
    x2 = None
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
    return 0, x1, x2


while True:
    cmd = input('> ').strip().split(' ')
    method, *args = cmd

    if method not in methods:
        code = 3
        print('Команда ' + method + ' не распознана.')
        print('Код ответа: {}'.format(code))
        continue

    if method == 'exit':
        exit()
        continue

    if method == 'login':
        code = 0
        try:
            code = login(*args)
            if code == 0:
                print('Авторизация прошла успешно.')
            else:
                print('Неправильное сочетание логина и пароля!')
        except TypeError:
            code = 1
            print('Введите логин и пароль!')
        finally:
            print('Код ответа: {}'.format(code))
            continue
    elif not authorized:
        code = 1
        print('Вы не авторизованы!')
        print('Код ответа: {}'.format(code))
        continue

    if method == 'store':
        try:
            code = store(*args)
            print('Коэффициенты записаны.')
        except TypeError:
            code = 2
            print('Укажите три коэффициента!')
        except:
            code = 3
            print('Коэффициенты - это числа!')
        finally:
            print('Код ответа: {}'.format(code))
            continue
    
    if method == 'solve':
        try:
            code, x1, x2 = solve(*args)
            if x1 is None:
                print('Рациональных корней нет.')
            else:
                print(f'Корни уравнения: {x1}, {x2}')
        except TypeError:
            code = 2
            print('Не указаны коэффициенты!')
        except:
            code = 3
            print('Коэффициенты - это числа!')
        finally:
            print('Код ответа: {}'.format(code))
        