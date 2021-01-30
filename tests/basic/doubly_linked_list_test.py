from unittest import TestCase

from basic.doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTest(TestCase):
    def test_doubly_linked_list(self):
        dll = DoublyLinkedList()
        for i in [5, 9, 3, 8, 9]:
            dll.add(i)

        print(f"size={dll.size}")
        dll.print_list()
        dll.remove(8)
        print(f"size after removing 8 is {dll.size}")

        print(dll.remove(15))
        print(dll.find(15))
        dll.add(21)
        dll.add(22)
        dll.remove(5)
        dll.print_list()
        print(dll.tail.pre)