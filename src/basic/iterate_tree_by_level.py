"""
Given A Binary Tree, print its values in level order such that there's a new line after every level
"""
from queue import Queue


class Node:
    def __init__(self, val, left=None, right=None, level=0):
        self.val = val
        self.left = left
        self.right = right
        self.level = level


root = Node(1,
            Node(2,
                 Node(4),
                 Node(5)),
            Node(3,
                 Node(6),
                 Node(7)))


def print_tree_in_level(node):
    if node is None:
        return
    current_level = 0
    q = Queue()
    q.put(node)
    while not q.empty():
        node = q.get()
        if node.level > current_level:
            print()
            current_level = node.level
        print(node.val, end='\t')
        if node.left is not None:
            node.left.level = current_level + 1
            q.put(node.left)
        if node.right is not None:
            node.right.level = current_level + 1
            q.put(node.right)


print_tree_in_level(root)
