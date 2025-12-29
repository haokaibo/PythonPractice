import math
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution
# 1. The leaf nodes are the operands. Numbers (positive integers)
# 2. The All the other nodes are operators.
# 3. There is always a valid expression tree, means for each operator nodes, it has both left and right children.

# Time complexity:
# O(n)
# Space complexity:
# O(h) -- For each level of the tree, the return value is well cached.
        
    
def calculate(node):
    # operator
    if node.value < 0:
        operator = node.value
        if operator == -1:
            # left node + right node
            return calculate(node.left) + calculate(node.right)
        elif operator == -2:
            # left node - right node
            return calculate(node.left) - calculate(node.right)
        elif operator == -3:
            # left node - right node
            return math.trunc(calculate(node.left) / calculate(node.right))
        elif operator == -4:
            # left node - right node
            return calculate(node.left) * calculate(node.right)
    else:
        return node.value

def evaluateExpressionTree(tree):
    # Write your code here.
    # call the internal function to calculate the operations.
    if tree is None:
        return -1

    return calculate(tree)
    
