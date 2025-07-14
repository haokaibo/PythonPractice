from threading import Thread, Lock
import time

database_value = 0
database_value2 = 0

def increase():
    global database_value

    local_copy = database_value
    local_copy +=1
    time.sleep(0.1)
    database_value = local_copy

def increase_with_lock(lock:Lock):
    global database_value2

    with lock:
        local_copy = database_value2
        local_copy += 1
        time.sleep(0.1)
        database_value2 = local_copy

if __name__=='__main__':

    print('start value')
    lock = Lock()
    thread1 = Thread(target=increase)
    thread2 = Thread(target=increase)

    thread3 = Thread(target=increase_with_lock, args=(lock,))
    thread4 = Thread(target=increase_with_lock, args=(lock,))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print(f'end value of database_value is {database_value}.')
    print(f'end value of database_value2 is {database_value2}.')

    print('end of main.')