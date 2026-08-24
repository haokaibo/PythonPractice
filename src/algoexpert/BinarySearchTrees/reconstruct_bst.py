# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Solution (Time: O(n), Space: O(n))
[10, 4, 2, 1, 3, 5, 17, 19, 18]
1. We start from the root 10 (Index 0)
2. The next element should be left -> 4(Index 1) 
pattern: if the current.value is less than the previous value it is the left child, the range is from float("-inf") to parent.value

elif the current.value is greater than or equals to the maxValue of the range(e.g. parent.parent.value), if could be a right node of upder level.
else: it should be the right child of the parent node.

"""
        
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    # nodeInfo = NodeInfo(0)

    # root node
    index = 0
    root = BST(preOrderTraversalValues[index])
    reconstructBstHelper(root, preOrderTraversalValues, index + 1, -float("inf"), float("inf"))
    return root

def reconstructBstHelper(parent, preOrderTraversalValues, index, minValue, maxValue):
    """
    Reconstruct BST from pre-order traversal values.

    Args:
        parent (BST): Parent node.
        preOrderTraversalValues (list): Pre-order traversal values.
        index (int): Current index.
        minValue (float): Minimum value of the range.
        maxValue (float): Maximum value of the range.

    Returns:
        int: Updated index.
    """
    # Base case: If index is out of range, return index
    if index >= len(preOrderTraversalValues):
        return index
    
    # Get the current value
    currentValue = preOrderTraversalValues[index]
    currentNode = BST(currentValue)
    
    # If the current value is less than the parent value, it should be the left child
    if currentValue < parent.value:
        parent.left = currentNode
        # Recursively update the index and reconstruct the left subtree
        index = reconstructBstHelper(currentNode, preOrderTraversalValues, index + 1, minValue, parent.value)
    
    # If index is out of range, return index
    if index >= len(preOrderTraversalValues):
        return index
    
    # Get the current value
    currentValue = preOrderTraversalValues[index]
    currentNode = BST(currentValue)
    
    # If the current value is greater than or equal to the parent value and less than the maxValue of the range,
    # it should be the right child of the parent node
    if currentValue < maxValue and currentValue >= parent.value:
        parent.right = currentNode
        # Recursively update the index and reconstruct the right subtree
        index = reconstructBstHelper(currentNode, preOrderTraversalValues, index + 1, parent.value, maxValue)
    
    # Return the updated index
    return index
    
