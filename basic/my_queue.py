from collections import deque


class Queue:
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

    def __str__(self):
        return str(self.queue)
