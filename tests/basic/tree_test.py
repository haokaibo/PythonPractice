from unittest import TestCase

from basic.tree import Tree


class TreeTest(TestCase):
    def test_tree(self):
        tree = Tree(7)
        for i in [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]:
            tree.insert(i)
        print(f'{"*" * 5}Finding nodes. {"*" * 5}')
        for i in range(16):
            print(tree.find(i), end=' ')
        print()

        print(f'{"*" * 5}Getting size. {"*" * 5}')
        print(f"The size of tree is {tree.get_size()}")

        print(f'{"*" * 5}Preordering tree. {"*" * 5}')
        tree.preorder()
        print()

        print(f'{"*" * 5}Inordering tree. {"*" * 5}')
        tree.inorder()
        print()
