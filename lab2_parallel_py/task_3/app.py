from pickle_worker import write_pickle
from shop_generator import generate_shop
from requester_seq import get_best_selling_laptops, get_most_expensive_videocards, get_best_employees
from requester_par import threading_par, multiprocessing_par

if __name__ ==  '__main__':
    write_pickle(generate_shop(), 'database.pkl')

    print(get_best_selling_laptops(1))
    print(get_most_expensive_videocards(5))
    print(get_best_employees(1))

    # для проверки
    # for lis in get_best_employees(100):
    #     print(lis[1][1] * 2 + lis[2][1])

    print()
    print()

    gbsl, gmev, gbe = threading_par(1, 5, 1)
    print(gbsl)
    print(gmev)
    print(gbe)

    print()
    print()

    gbsl, gmev, gbe = multiprocessing_par(1, 5, 1)
    print(gbsl)
    print(gmev)
    print(gbe)