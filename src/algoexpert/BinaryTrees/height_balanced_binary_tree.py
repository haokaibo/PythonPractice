# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, height, balanced):
        self.height = height
        self.balanced = balanced
        
"""
Solution(Time: O(n), Space: O(h))
Iterate the tree from the top to the bottom.
Check the children nodes count for both side if the gap is greater than 1 then it is not balanced
"""
def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = checkBinaryTreeHeight(tree)
    return treeInfo.balanced

def checkBinaryTreeHeight(tree):
    if tree is None:
        return TreeInfo(0, True)

    leftTreeInfo = checkBinaryTreeHeight(tree.left)
    rightTreeInfo = checkBinaryTreeHeight(tree.right)
    
    leftHeight = leftTreeInfo.height
    rightHeight = rightTreeInfo.height
    
    balanced = leftTreeInfo.balanced and rightTreeInfo.balanced and abs(leftHeight - rightHeight) <= 1
    return TreeInfo(max(leftHeight, rightHeight) + 1, balanced)