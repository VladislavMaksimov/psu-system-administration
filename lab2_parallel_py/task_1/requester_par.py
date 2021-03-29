import requester_seq
from threading import Thread
from multiprocessing import Process, Manager, Queue

def threading_par(count):
    gbs_list = []
    gbt_list = []
    ghs_list = []

    gbs_thread = Thread(target=gbs_wrapper, args=(count,gbs_list))
    gbt_thread = Thread(target=gbt_wrapper, args=(count,gbt_list))
    ghs_thread = Thread(target=ghs_wrapper, args=(count,ghs_list))

    gbs_thread.start()
    gbt_thread.start()
    ghs_thread.start()
    gbs_thread.join()
    gbt_thread.join()
    ghs_thread.join()

    return (gbs_list, gbt_list, ghs_list)

def multiprocessing_par(count):
    gbs_queue = Queue()
    gbt_queue = Queue()
    ghs_queue = Queue()

    gbs_process = Process(target=gbs_wrapper_pr, args=(count,gbs_queue))
    gbt_process = Process(target=gbt_wrapper_pr, args=(count,gbt_queue))
    ghs_process= Process(target=ghs_wrapper_pr, args=(count,ghs_queue))

    gbs_process.start()
    gbt_process.start()
    ghs_process.start()
    gbs_process.join()
    gbt_process.join()
    ghs_process.join()

    return (gbs_queue.get(), gbt_queue.get(), ghs_queue.get())

# обёртки для получения значений при распараллеливании потоками
def gbs_wrapper(count, result):
    result.extend(requester_seq.get_best_students(count))

def gbt_wrapper(count, result):
    result.extend(requester_seq.get_best_truants(count))

def ghs_wrapper(count, result):
    result.extend(requester_seq.get_heardest_subjects(count))

# обёртки для получения значений при распараллеливании процессами
def gbs_wrapper_pr(count, result):
    result.put(requester_seq.get_best_students(count))

def gbt_wrapper_pr(count, result):
    result.put(requester_seq.get_best_truants(count))

def ghs_wrapper_pr(count, result):
    result.put(requester_seq.get_heardest_subjects(count))