from json_worker import write_json
from autos_generator import generate_dictionary
from requester_seq import get_best_selling_auto, get_most_expensive_parts, get_most_effective_employees
from requester_par import threading_par, timer_par

write_json(generate_dictionary(), 'database.json')

print("==== ПОСЛЕДОВАТЕЛЬНЫЕ ЗАПРОСЫ ====")

print("\nСамая продаваемая машина:\n")
print(get_best_selling_auto(1))
print("\n5 самых дорогих запчастей:\n")
print(get_most_expensive_parts(5))
print("\nСамый эффективный сотрудник:\n")
print(get_most_effective_employees(1))

print()
print()

print("==== РАСПАРАЛЛЕЛИВАНИЕ ПОТОКАМИ ====")

gbsa, gmep, gmee = threading_par(1, 5, 1)
print("\nСамая продаваемая машина:\n")
print(gbsa)
print("\n5 самых дорогих запчастей:\n")
print(gmep)
print("\nСамый эффективный сотрудник:\n")
print(gmee)

print()
print()

print("==== РАСПАРАЛЛЕЛИВАНИЕ ПРОЦЕССАМИ ====")

gbsa, gmep, gmee = timer_par(1, 5, 1)
print("\nСамая продаваемая машина:\n")
print(gbsa)
print("\n5 самых дорогих запчастей:\n")
print(gmep)
print("\nСамый эффективный сотрудник:\n")
print(gmee)