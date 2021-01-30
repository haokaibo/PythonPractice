from unittest import TestCase

from basic.linked_list import LinkedList


class LinkedListTest(TestCase):
    l = LinkedList()
    l.add(5).add(8).add(12)
    l.print_list()

    print(f"size={l.size}")
    l.remove(8)
    print(f'size={l.size}\n')
    print(l.find(5))
    print(l.root)