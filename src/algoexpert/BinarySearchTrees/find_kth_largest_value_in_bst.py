# This is an input class. Do not edit.
"""
Solution(Time: O(h + k), Space: O(h)) h is the height of the tree. k is the kth value
1. Iterate the right most child in the bottom of the tree.
2. Reverse iterate the path from the right most child to its parent node and left sibling.
"""
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class NodeInfo:
    def __init__(self, nth, value):
        self.nth = nth
        self.value = value

def findKthLargestValueInBstHelper(tree, k, nodeInfo):
    if tree is None or nodeInfo.nth >= k:
        return

    findKthLargestValueInBstHelper(tree.right, k, nodeInfo)

    if nodeInfo.nth < k:
        nodeInfo.nth += 1
        nodeInfo.value = tree.value
        findKthLargestValueInBstHelper(tree.left, k, nodeInfo)
   

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    nodeInfo = NodeInfo(0, -1)
    findKthLargestValueInBstHelper(tree, k, nodeInfo)
    
    return nodeInfo.value