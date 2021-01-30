from unittest import TestCase

from basic.circular_linked_list import CircularLinkedList


class CircularLinkedListTest(TestCase):
    def test_circular_linked_list(self):
        cll = CircularLinkedList()
        for i in [5, 7, 3, 8, 9]:
            cll.add(i)
        print(f"size={cll.size}\n{cll.find(8)}\n{cll.find(12)}")

        my_node = cll.root
        print(my_node, end='->')
        for i in range(8):
            my_node = my_node.nxt
            print(my_node, end='->')
        print()