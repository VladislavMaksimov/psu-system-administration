from requester_seq import get_best_selling_laptops, get_most_expensive_videocards, get_best_employees

from threading import Thread
from multiprocessing import Process, Manager, Queue

def threading_par(gbsl_count, gmev_count, gbe_count):
    gbsl_list = []
    gmev_list = []
    gbe_list = []

    gbsl_thread = Thread(target=gbsl_wrapper, args=(gbsl_count,gbsl_list))
    gmev_thread = Thread(target=gmev_wrapper, args=(gmev_count,gmev_list))
    gbe_thread = Thread(target=gbe_wrapper, args=(gbe_count,gbe_list))

    gbsl_thread.start()
    gmev_thread.start()
    gbe_thread.start()
    gbsl_thread.join()
    gmev_thread.join()
    gbe_thread.join()

    return (gbsl_list, gmev_list, gbe_list)

def multiprocessing_par(gbsl_count, gmev_count, gbe_count):
    gbsl_queue = Queue()
    gmev_queue = Queue()
    gbe_queue = Queue()

    gbsl_process = Process(target=gbsl_wrapper_pr, args=(gbsl_count,gbsl_queue))
    gmev_process = Process(target=gmev_wrapper_pr, args=(gmev_count,gmev_queue))
    gbe_process= Process(target=gbe_wrapper_pr, args=(gbe_count,gbe_queue))

    gbsl_process.start()
    gmev_process.start()
    gbe_process.start()
    gbsl_process.join()
    gmev_process.join()
    gbe_process.join()

    return (gbsl_queue.get(), gmev_queue.get(), gbe_queue.get())

# обёртки для получения значений при распараллеливании потоками
def gbsl_wrapper(count, result):
    result.extend(get_best_selling_laptops(count))

def gmev_wrapper(count, result):
    result.extend(get_most_expensive_videocards(count))

def gbe_wrapper(count, result):
    result.extend(get_best_employees(count))

# обёртки для получения значений при распараллеливании процессами
def gbsl_wrapper_pr(count, result):
    result.put(get_best_selling_laptops(count))

def gmev_wrapper_pr(count, result):
    result.put(get_most_expensive_videocards(count))

def gbe_wrapper_pr(count, result):
    result.put(get_best_employees(count))