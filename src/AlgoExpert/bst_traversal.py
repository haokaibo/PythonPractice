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
