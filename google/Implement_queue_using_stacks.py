"""
Implement a queue using stacks (with a twist at the end)
"""
from collections import deque

print("Implementing Queue by Two stacks.")


class QueueByTwoStacks:
    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()
        self.out_stack_len = 0
        self.in_stack_len = 0

    def push(self, val):
        self.in_stack.append(val)
        self.in_stack_len += 1

    def pop(self):
        if self.out_stack_len > 0:
            self.out_stack_len -= 1
            return self.out_stack.pop()
        else:
            if self.in_stack_len > 0:
                # pop every element from in_stack and push to the out_stack
                while self.in_stack_len > 1:
                    self.out_stack.append(self.in_stack.pop())
                    self.in_stack_len -= 1
                    self.out_stack_len += 1
                self.in_stack_len -= 1
                return self.in_stack.pop()
            else:
                return None

    def empty(self):
        return self.in_stack_len == 0 and self.out_stack_len == 0


q = QueueByTwoStacks()
for i in range(10):
    q.push(i)

while not q.empty():
    print(q.pop())

print("Impelementing Queue by One Single stack.")


class QueueBySingleStack():
    def __init__(self):
        self.stack = deque()
        self.size = 0

    def push(self, val):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        if self.size == 1:
            self.size -= 1
            return self.stack.pop()

        # key step 1 - get current node value
        cur_val = self.stack.pop()
        self.size -= 1

        # key step 2 - recursive call the pop to the end of the stack
        result = self.pop()

        # key step 3 - push the current value back to the stack
        self.push(cur_val)
        return result

    def empty(self):
        return self.size == 0


q = QueueBySingleStack()
for i in range(10):
    q.push(i)

while not q.empty():
    print(q.pop())
