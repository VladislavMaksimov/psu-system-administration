from json_worker import write_json
from students_generator import generate_students
from requester_par import threading_par, multiprocessing_par

import requester_seq
# условие, без которого в винде подпроцессы будут выполнять основной модуль и вызывать новые подпроцессы
if __name__ ==  '__main__':
    write_json(generate_students(), 'database.json')

    print("==== ПОСЛЕДОВАТЕЛЬНЫЕ ЗАПРОСЫ ====")

    print("\nТоп-10 по успеваемости:\n")
    print(requester_seq.get_best_students(10))
    print("\nТоп-10 по прогулам:\n")
    print(requester_seq.get_best_truants(10))
    print("\nТоп-10 самых трудных предметов:\n")
    print(requester_seq.get_heardest_subjects(10))

    print()
    print()

    print("==== РАСПАРАЛЛЕЛИВАНИЕ ПОТОКАМИ ====")

    gbs, gbt, ghs = threading_par(10)
    print("\nТоп-10 по успеваемости:\n")
    print(gbs)
    print("\nТоп-10 по прогулам:\n")
    print(gbt)
    print("\nТоп-10 самых трудных предметов:\n")
    print(ghs)

    print()
    print()

    print("==== РАСПАРАЛЛЕЛИВАНИЕ ПРОЦЕССАМИ ====")

    gbs, gbt, ghs = multiprocessing_par(10)
    print("\nТоп-10 по успеваемости:\n")
    print(gbs)
    print("\nТоп-10 по прогулам:\n")
    print(gbt)
    print("\nТоп-10 самых трудных предметов:\n")
    print(ghs)