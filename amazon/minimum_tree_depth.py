"""
Given a binary tree. find its minimus depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
    3
   /  \
  9   20
     /  \
    15   7

BFS iteration
create a class Node with val, left, right and depth
create a queue to cache each level's nodes
iterate each level till find a node without child just return the node.depth
"""
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None, depth=0):
        self.val = val
        self.left = left
        self.right = right
        self.depth = depth

    def __str__(self):
        return str(self.val)


class Solution:
    def __init__(self, root):
        self.root = root
        self.queue = deque()
        if root is not None:
            root.depth = 1
            self.queue.append(root)

    def get_minimum_depth(self):
        while len(self.queue) > 0:
            node = self.queue.pop()
            if node.left is None and node.right is None:  # find the first the no child node
                return node.depth
            elif node.left is not None:
                node.left.depth = node.depth + 1
                self.queue.append(node.left)
            elif node.right is not None:
                node.right.depth = node.depth + 1
                self.queue.append(node.right)
        return 0


root = Node(3,
            Node(9),
            Node(20,
                 Node(15), Node(7)))

solution = Solution(root)
print(solution.get_minimum_depth())
