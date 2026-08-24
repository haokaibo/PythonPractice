# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Solution(Time: O(n), Space: O(n))
1. Iterate the tree to get each node's left sum and right sum and stored 
in a dict
2. Iterate the tree info to calculate the parent, check
The total = 2 * leftSum or total = 2 * rightSum
Use a dict to hold the left/right sum.
Check the total / 2 is in the dict
"""    
def calculateSum(tree, sumDict):
    if tree is None:
        return 0
    
    leftSum = calculateSum(tree.left, sumDict)
    if leftSum not in sumDict:
        sumDict[leftSum] = 0
    sumDict[leftSum] += 1  
    
    rightSum = calculateSum(tree.right, sumDict)
    if rightSum not in sumDict:
        sumDict[rightSum] = 0
    sumDict[rightSum] += 1  

    return tree.value + leftSum + rightSum
    
def splitBinaryTree(tree):
    # Write your code here.
    treeSum = dict()
    treeTotal = calculateSum(tree, treeSum)
    if treeTotal / 2 in treeSum:
        return treeTotal / 2
    else:
        return 0