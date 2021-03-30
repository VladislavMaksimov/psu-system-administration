from pickle_worker import write_pickle
from shop_generator import generate_shop
from requester_seq import get_best_selling_laptops, get_most_expensive_videocards, get_best_employees
from requester_par import threading_par, multiprocessing_par

if __name__ ==  '__main__':
    write_pickle(generate_shop(), 'database.pkl')

    print("==== ПОСЛЕДОВАТЕЛЬНЫЕ ЗАПРОСЫ ====")

    print("\nСамая продаваемая модель ноутбука:\n")
    print(get_best_selling_laptops(1))
    print("\n5 самых дорогих видеокарт:\n")
    print(get_most_expensive_videocards(5))
    print("\nСамый эффективный сотрудник:\n")
    print(get_best_employees(1))

    # для проверки
    # for lis in get_best_employees(100):
    #     print(lis[1][1] * 2 + lis[2][1])

    print()
    print()

    print("==== РАСПАРАЛЛЕЛИВАНИЕ ПОТОКАМИ ====")

    gbsl, gmev, gbe = threading_par(1, 5, 1)
    print("\nСамая продаваемая модель ноутбука:\n")
    print(gbsl)
    print("\n5 самых дорогих видеокарт:\n")
    print(gmev)
    print("\nСамый эффективный сотрудник:\n")
    print(gbe)

    print()
    print()

    print("==== РАСПАРАЛЛЕЛИВАНИЕ ПРОЦЕССАМИ ====")

    gbsl, gmev, gbe = multiprocessing_par(1, 5, 1)
    print("\nСамая продаваемая модель ноутбука:\n")
    print(gbsl)
    print("\n5 самых дорогих видеокарт:\n")
    print(gmev)
    print("\nСамый эффективный сотрудник:\n")
    print(gbe)