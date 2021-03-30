from random import randint

laptops = [
    'ASUS 1',
    'ASUS 2',
    'ASUS 3',
    'ASUS 4',
    'ASUS 5',
    'ASUS 6',
    'Lenovo 1',
    'Lenovo 2',
    'Lenovo 3',
    'Lenovo 4',
    'Lenovo 5',
    'Lenovo 6',
    'ACER 1',
    'ACER 2',
    'ACER 3',
    'ACER 4',
    'ACER 5',
    'ACER 6'
]

videocards = [
    'NVIDIA GeForce RTX 2080 Ti',
    'NVIDIA Titan RTX',
    'AMD Radeon VII',
    'Intel Iris Plus Graphics G4',
    'ATI Radeon HD 4860',
    'NVIDIA Quadro K2100M',
    'AMD FirePro M6000',
    'Intel GMA 3150',
    'NVIDIA Quadro NVS 140M',
    'NVIDIA NVS 3100M',
    'ATI Mobility Radeon HD 4550',
    'NVIDIA GeForce 9300M G'
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

def generate_laptop(laptop):
    price = randint(1, 5) * 10000
    sold_laptops = randint(0, 30)
    laptop_list = [
        ['name', laptop],
        ['price', price],
        ['sold_laptops', sold_laptops]        
    ]
    return laptop_list

def generate_videocard(videocard):
    price = randint(1, 5) * 3000
    videocard_list = [
        ['name', videocard],
        ['price', price]
    ]
    return videocard_list

def generate_employee(employee):
    laptops_sold = randint(0, 20)
    videocards_sold = randint(0, 40)
    employee_list = [
        ['name', employee],
        ['laptops_sold', laptops_sold],
        ['videocards_sold', videocards_sold]
    ]
    return employee_list

def generate_shop():
    shop = [
        ['laptops', []],
        ['videocards', []],
        ['employees', []]
    ]

    laptops_list = shop[0][1]
    videocards_list = shop[1][1]
    employees_list = shop[2][1]

    for laptop in laptops:
        laptops_list.append(generate_laptop(laptop))
    for videocard in videocards:
        videocards_list.append(generate_videocard(videocard))
    for employee in employees:
        employees_list.append(generate_employee(employee))

    return shop