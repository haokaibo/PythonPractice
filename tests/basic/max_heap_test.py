from basic.max_heap import MaxHeap
from unittest import TestCase


class MaxHeapTest(TestCase):
    def test_pop(self):
        h = MaxHeap(items=[1, 2, 3, 4, 5])
        print(h)
        assert h.pop() == 5
        print(h)
