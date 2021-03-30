from pickle_worker import read_pickle

# получает самые продаваемые модели ноутбуков
def get_best_selling_laptops(count):
    shop = read_pickle('database.pkl')
    laptops = shop[0][1]
    laptops.sort(key=lambda lis: lis[2][1], reverse=True)
    return laptops[0:count]

# получает самые дорогие видеокарты
def get_most_expensive_videocards(count):
    shop = read_pickle('database.pkl')
    videocards = shop[1][1]
    videocards.sort(key=lambda lis: lis[1][1], reverse=True)
    return videocards[0:count]

# получает самых эффективных сотрудников
def get_best_employees(count):
    shop = read_pickle('database.pkl')
    employees = shop[2][1]
    employees.sort(key=lambda lis: lis[1][1] * 2 + lis[2][1], reverse=True)
    return employees[0:count]