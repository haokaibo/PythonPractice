with open('notes1.txt', 'a+') as file:
    file.write('some to doo...\n')

file = open('notes1.txt', 'a+')
try:
    file.write('some to to doo...\n')
finally:
    file.close()

# multi threading.
from threading import Lock
lock =Lock()
with lock:
    print('Working..')

lock.acquire()
print('working..')
lock.release()

#
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'a+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        # print(f'exc: {exc_type, exc_val}')
        print('exit')
        return True

with ManagedFile('notes1.txt') as file:
    print('do some stuff..')
    file.write('some to doo...\n')
    file.somemethod()

print('continuing..')

# context manager
from contextlib import contextmanager
@ contextmanager
def open_managed_file(filename):
    f=open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes2.txt') as f:
    f.write('something to do...')