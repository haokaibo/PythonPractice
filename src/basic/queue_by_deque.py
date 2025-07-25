from collections import deque


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