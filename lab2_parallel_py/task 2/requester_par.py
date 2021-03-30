import requester_seq
from threading import Thread, Timer

def threading_par(gbsa_count, gmep_count, gmee_count):
    gbsa_list = []
    gmep_list = []
    gmee_list = []

    gbsa_thread = Thread(target=gbsa_wrapper, args=(gbsa_count,gbsa_list))
    gmep_thread = Thread(target=gmep_wrapper, args=(gmep_count,gmep_list))
    gmee_thread = Thread(target=gmee_wrapper, args=(gmee_count,gmee_list))

    gbsa_thread.start()
    gmep_thread.start()
    gmee_thread.start()
    gbsa_thread.join()
    gmep_thread.join()
    gmee_thread.join()

    return (gbsa_list, gmep_list, gmee_list)

def timer_par(gbsa_count, gmep_count, gmee_count):
    gbsa_list = []
    gmep_list = []
    gmee_list = []

    gbsa_timer = Timer(1.0, gbsa_wrapper, (gbsa_count,gbsa_list))
    gmep_timer = Timer(0.5, gmep_wrapper, (gmep_count,gmep_list))
    gmee_timer = Timer(0.1, gmee_wrapper, (gmee_count,gmee_list))

    gbsa_timer.start()
    gmep_timer.start()
    gmee_timer.start()
    gbsa_timer.join()
    gmep_timer.join()
    gmee_timer.join()

    return (gbsa_list, gmep_list, gmee_list)

def gbsa_wrapper(count, result):
    result.extend(requester_seq.get_best_selling_auto(count))

def gmep_wrapper(count, result):
    result.extend(requester_seq.get_most_expensive_parts(count))

def gmee_wrapper(count, result):
    result.extend(requester_seq.get_most_effective_employees(count))