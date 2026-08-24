"""
Binary Tree Diameter

You're given a binary tree. Write a function that returns the diameter of
the binary tree.

The diameter of a binary tree is the length of the longest path between any
two nodes in the tree. A path is a sequence of nodes where each pair of
consecutive nodes in the sequence must be connected by an edge. The length
of a path is the number of edges in the path (equivalently, the number of
nodes in the path minus one).
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Solution(Time: O(n), Space: O(n)) / on average O(h) , h is the height of the tree.
Iterate the tree nodes from the top to the bottom. For each node which has 
two children nodes, sum the left and right max length for the best path.
Use a class to hold the current best diameter, and longest single path from 
the current node to one its descendants leave node.
"""
def binaryTreeDiameter(tree):
    # Write your code here.
    nodeInfo = binaryTreeDiameterHelper(tree)
    return nodeInfo.diameter

class NodeInfo:
    def __init__(self, diameter, longestPath):
        self.diameter = diameter
        self.longestPath = longestPath
    
def binaryTreeDiameterHelper(tree):
    nodeInfo = NodeInfo(0, 0)
    if tree is None:
        return nodeInfo

    leftNodeInfo = NodeInfo(0, 0)
    if tree.left is not None:
        leftNodeInfo = binaryTreeDiameterHelper(tree.left)
        leftNodeInfo.longestPath += 1

    rightNodeInfo = NodeInfo(0, 0)
    if tree.right is not None:
        rightNodeInfo = binaryTreeDiameterHelper(tree.right)
        rightNodeInfo.longestPath += 1

    nodeInfo.longestPath = max(leftNodeInfo.longestPath, rightNodeInfo.longestPath)
    currentDiameter = leftNodeInfo.longestPath + rightNodeInfo.longestPath
    nodeInfo.diameter = max(currentDiameter, leftNodeInfo.diameter, rightNodeInfo.diameter)        
    
    return nodeInfo
    