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
        print(f'\n{"*" * 5} Testing remove {"*" * 5}')

        cll.print_list()
        print('removing 8 from list.')
        cll.remove(8)
        cll.print_list()
        print(f"removing 15 from list. Result is {cll.remove(15)}")
        print(f'size={cll.size}')
        cll.print_list()
        cll.remove(5)
        cll.print_list()
