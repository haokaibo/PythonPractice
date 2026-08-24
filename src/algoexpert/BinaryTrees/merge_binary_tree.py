"""
Merge Binary Tree

You're given two binary trees. Write a function that merges the two binary
trees into a single binary tree.

When merging, the values of overlapping nodes (nodes at the same position in
both trees) are summed. If a node exists in only one of the two trees, it is
kept as-is in the merged tree. The function should return the root of the
merged binary tree.
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Solution(Time: O(n), Space: O(h)) n is the node count of the smaller Binary Tree, h is the height of the smaller tree.
"""
def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None:
        return tree2
    if tree2 is None:
        return tree1

    tree1.value += tree2.value
    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
    
    return tree1
