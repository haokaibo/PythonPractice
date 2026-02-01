# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

"""
Solution(Time: O(n), Space: O(h))
Use the recursive function to check the symmetric recursively. 
"""
def checkSymmetrical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
        
    if tree1 is None or tree2 is None:
        return False
        
    if tree1.value != tree2.value:
        return False

    if not checkSymmetrical(tree1.left, tree2.right):
        return False

    if not checkSymmetrical(tree1.right, tree2.left):
        return False

    return True

def symmetricalTree(tree):
    # Write your code here.
    if tree is None:
        return False
    return checkSymmetrical(tree.left, tree.right)
