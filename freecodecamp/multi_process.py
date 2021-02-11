from multiprocessing import Process, Value, Array, Lock
from queue import Queue
import time

def add_100(value, arr, numbers, q, lock1, lock2):
    for i in range(100):
        time.sleep(0.01)
        with lock1:
            value.value+=1
        with lock2:
            for j in range(len(arr)):
                arr[j] +=1

        for i in numbers:
            q.put(i*i)

if __name__ == '__main__':
    lock1 =Lock()
    lock2 = Lock()
    shared_value = Value('i', 0) # "i" indicates the type int
    shared_array = Array('d', [0.0, 100.0, 200.0]) # "d" indicates the type decimal
    shared_numbers = range(1,6)
    q = Queue()

    print('shared_value at the beginning is', shared_value.value)
    print('shared_array at the beginning is', shared_array[:])

    p1 = Process(target=add_100, args=(shared_value, shared_array,shared_numbers, q, lock1 ,lock2))
    p2 = Process(target=add_100, args=(shared_value, shared_array,shared_numbers, q, lock1 ,lock2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f'The final shared_value is {shared_value.value}')
    print(f'The final shared_array is {shared_array[:]}')

    while not q.empty():
        print(q.get())