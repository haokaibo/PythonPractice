# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

"""
Solution(Time: O(h), Space: O(1))
"""
def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        return findTheLeftmostChild(node.right)

    else:
        return findTheFirstRightParent(node)

def findTheLeftmostChild(node):
    current = node
    while current.left is not None:
        current = current.left

    return current

def findTheFirstRightParent(node):
    current = node
    while current.parent is not None and current.parent.right == current:
        current = current.parent

    return current.parent