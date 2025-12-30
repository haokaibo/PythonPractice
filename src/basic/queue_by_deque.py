from collections import deque

import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))  # project root
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

class QueueByDeque:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) < 0:
            return None
        else:
            return self.queue.popleft()

    def peek(self):
        if len(self.queue) < 0:
            return None
        else:
            return self.queue[0]

    def last(self):
        if len(self.queue) < 0:
            return None
        else:
            return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


q = QueueByDeque()
q.push(1)
q.push(2)
print(f"q.peek()={q.peek()}")
print(f"q={q}")
print(f"q.last()={q.last()}")
print(f"q.empty()={q.empty()}")

lastNode = 1
a= 2 if lastNode == None else 3
print(a)

2 if 1==2 else 3