'''
Process: An instance of a program (e.g a Python interpreter)

+ Takes advantage of multiple CPUs and cores
+ Separate memory space -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is started independently from other processes
+ Processes are interruptable/killable
+ One GIL for each process -> avoids GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread.
- More memory
- IPC (inter-process communication) is more complicated

Threads: An entity within a process that can be scheduled (also known as "leightweight" process)
A process can spawn multiple threads.

+ All threads within a process share the same memory
+ Leightweight
+ Starting a tread is faster than starting a process
+ Great for I/O-bound tasks

- Threading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks
- Not interruptable/killable
- Careful with race conditions

GIL: Global interpreter lock
- A lock that allows only one thread at a tie to execute in Python

- Needed in CPython because memory management is not thread-safe

- Avoid
    - Use multiprocessing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
'''


from multiprocessing import Process
import os, time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

print(f'num_processes={num_processes}')

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print('end main')