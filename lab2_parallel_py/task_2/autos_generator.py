from random import randint

autos = [
    'Audi 1',
    'Lada 1',
    'Audi 2',
    'Lada 2',
    'Mercedes 1',
    'Mercedes 2',
    'Mercedes 3',
    'Ferrari 1',
    'Ferrari 2'
]

employees = [
    'Damir',
    'Kirill',
    'Irina',
    'Vlad',
    'Nastya',
    'Danil',
    'Misha',
    'Andrey',
    'Kristina',
    'Oleg',
    'Vladimir',
    'Alexey',
    'John Doe',
    'Felix',
    'Arsen'
]

parts = [
    'steering wheel',
    'wheel',
    'engine',
    'mirror',
    'headlight',
    'glass',
    'generator',
    'brake discs',
    'camshaft sensor',
    'wishbone',
    'crankshaft oil seals'
]

def generate_auto(auto):
    price = randint(1, 4) * 1000000
    cars_sold = randint(20, 50)
    auto_struct = {
        'name': auto,
        'price': price,
        'cars_sold': cars_sold
    }
    return auto_struct

def generate_employee(employee):
    sold_cars = randint(10, 30)
    employee_struct = {
        'name': employee,
        'sold_cars': sold_cars,
    }
    return employee_struct

def generate_part(part):
    price = randint(2, 20) * 1000
    part_struct = {
        'name': part,
        'price': price
    }
    return part_struct

def generate_dictionary():
    dictionary = dict()
    dictionary['autos'] = dict()
    dictionary['employees'] = dict()
    dictionary['parts'] = dict()

    autos_dict = dictionary['autos']
    for auto in autos:
        autos_dict[id(auto)] = generate_auto(auto)
    
    employees_dict = dictionary['employees']
    for employee in employees:
        employees_dict[id(employee)] = generate_employee(employee)

    parts_dict = dictionary['parts']
    for part in parts:
        parts_dict[id(part)] = generate_part(part)

    return dictionary