from json_worker import read_json

# получает самые продаваемые машины
def get_best_selling_auto(count):
    dictionary = read_json('database.json')
    autos = dictionary['autos']
    autos_sorted_list = []

    for auto in autos.items():
        name = auto[1]['name']
        cars_sold = auto[1]['cars_sold']
        autos_sorted_list.append((name, cars_sold))

    autos_sorted_list.sort(key=lambda tup: tup[1], reverse=True)
    return autos_sorted_list[0:count]

# получает самые дорогие запчасти
def get_most_expensive_parts(count):
    dictionary = read_json('database.json')
    parts = dictionary['parts']
    parts_sorted_list = []

    for part in parts.items():
        name = part[1]['name']
        price = part[1]['price']
        parts_sorted_list.append((name, price))

    parts_sorted_list.sort(key=lambda tup: tup[1], reverse=True)
    return parts_sorted_list[0:count]

# получает самых эффективных сотрудников
def get_most_effective_employees(count):
    dictionary = read_json('database.json')
    employees = dictionary['employees']
    employees_sorted_list = []

    for employee in employees.items():
        name = employee[1]['name']
        sold_cars = employee[1]['sold_cars']
        employees_sorted_list.append((name, sold_cars))

    employees_sorted_list.sort(key=lambda tup: tup[1], reverse=True)
    return employees_sorted_list[0:count]