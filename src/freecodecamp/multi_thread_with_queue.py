from queue import Queue
from threading import Thread, Lock, current_thread


def worker(q: Queue, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}.')
        q.task_done()
        # if something happen:
        #     break

if __name__ == '__main__':
    q = Queue()

    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon = True
        thread.start()

    for i in range(1,21):
        q.put(i)

    q.join()
