"""
1) Binary Search Tree(BST) have the following property: Left< Root < Right
2) An in-order traversal would result in visiting the nodes in sorted, ascending order(smallest->largest).

Given any node in a BST, get the in-order successor to that node.
The successor is the next node in the traversal.
You can assume the node is valid and exists somewhere in the tree
        4
     /    \
    2      6
   / \    / \
  1   3  5   7

given node: 4(has right)                                                       5 (no right node and is left child)    7 (no right nod and is right child)
successor:  5(The most left ascendant of right child or right node)            6 (5's parent node)                    None

input:      root, node
output:     successor_node

1. find the parent node by find_parent_node(root, node)

2. find successor:
    if node.right is not None:  # has right child node, find the left most descendant or self
        temp = node.right
        while temp.left is not None:
            temp = temp.left
        return temp
    else:  # no right child node
        if parent_node is None or node.val > parent_node.val:  # is the right child of parent
            return None
        else:  # is the left child of parent
            return parent_node

time: find parent node O(log(n)) -> O(d) d is the depth where the node exists
space: O(log(n))
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    @staticmethod
    def find_parent_node(root: Node, node: Node, parent_node: Node):
        if node is None or root is None:
            return None
        elif node.val == root.val:
            return parent_node
        elif node.val > root.val:
            return Solution.find_parent_node(root.right, node, root)
        else:
            return Solution.find_parent_node(root.left, node, root)

    @staticmethod
    def find_successor(root: Node, node: Node):
        parent_node = Solution.find_parent_node(root, node, None)
        if node.right is not None:  # has right child node, find the left most descendant or self
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            return temp
        else:  # no right child node
            if parent_node is None or node.val > parent_node.val:  # parent node is none(the node is the root)
                                                                   # is the right child of parent
                return None
            else:  # is the left child of parent
                return parent_node


"""
       4
     /    \
    2      6
   / \    /  \
  1   3  5    7
"""
root = Node(4,
            Node(2,
                 Node(1),
                 Node(3)),
            Node(6,
                 Node(5),
                 Node(7)))

print(f"{root} -> {Solution.find_successor(root, root)}")  # 4 - > 5
print(f"{root.right.left} -> {Solution.find_successor(root, root.right.left)}")  # 5 -> 6
print(f"{root.right} -> {Solution.find_successor(root, root.right)}") # 6 -> 7
print(f"{root.right.right} -> {Solution.find_successor(root, root.right.right)}") # 7 -> None

# test edge case there is no parent_node and there is no right node
"""
4
"""
root = Node(4)
print(f"{root} -> {Solution.find_successor(root, root)}")


"""
       40
     /    \
    2      60
   / \    /  \
  1   3  50   70
             /
            65
"""
root = Node(40,
            Node(2,
                 Node(1),
                 Node(3)),
            Node(60,
                 Node(50),
                 Node(70, Node(65))))
print(f"{root} -> {Solution.find_successor(root, root.right)}") # 60 -> 65
print(f"{root} -> {Solution.find_successor(root, root.right.right)}") # 70 -> None