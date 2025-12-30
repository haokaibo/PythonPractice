from unittest import TestCase

from basic.queue_by_deque import QueueByDeque


class QueueTest(TestCase):
    def test_pop(self):
        q = QueueByDeque()
        q.push(1)
        q.push(2)
        print(f"The origin queue={q}.")
        return_val = q.pop()
        print(f"The one has been popped={return_val}.")
        print(f"The queue popped={q}")

    def test_peek(self):
        q = QueueByDeque()
        q.push(1)
        q.push(2)
        print(f"The origin queue={q}.")
        assert q.peek() == 1
        print(f"The one has been peeked={q.peek()}.")
        print(f"The queue peeked={q}.")
