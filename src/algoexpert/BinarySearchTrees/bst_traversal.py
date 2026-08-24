"""
BST Traversal

You're given a Binary Search Tree with at least one node. Write a function
that takes in the tree's root node and returns an array containing the
in-order traversal of the BST's nodes, where each node in the array is
represented by the value of its node.

More specifically, the in-order traversal of a BST is the traversal of the
BST according to the following rules: at any given point in time, the first
node to be traversed is the leftmost node in the tree. Then, once a node has
been traversed, there are two choices: if the node has a right sibling, the
right sibling becomes the next node to be traversed. Otherwise, we go back
up to the first traversed node's parent, and, if that node has
yet-untraversed siblings, the first of those siblings becomes the next node
to be traversed. Otherwise, we keep going back up the tree until we either
find a node with yet-untraversed siblings or we completely run out of nodes.
In other words, a fully traversed node should have both its left and right
sibling traversed (if either of those two nodes exist).

Note that the root node can also be a left or right sibling.
"""

"""
Solution(Time: O(n), Space: O(n))
inOrder: Iterate the left first, then current, then right
"""
def inOrderTraverse(tree, array):
    # Write your code here.
    # Check empty node
    if tree is None:
        return array

    if tree.left is not None:
        inOrderTraverse(tree.left, array)

    array.append(tree.value)

    if tree.right is not None:
        inOrderTraverse(tree.right, array)

    return array
    


def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array

    array.append(tree.value)

    if tree.left is not None:
        preOrderTraverse(tree.left, array)

    if tree.right is not None:
        preOrderTraverse(tree.right, array)

    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array

    if tree.left is not None:
        postOrderTraverse(tree.left, array)

    if tree.right is not None:
        postOrderTraverse(tree.right, array)

    array.append(tree.value)

    return array
