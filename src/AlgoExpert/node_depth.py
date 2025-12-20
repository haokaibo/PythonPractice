# Solution
## 1. Iterate the tree from the root
## 2. Each each node, we can iterate its left and right Descendants, 
# then sum its Descendants path depth, plus its own depth as the return
## 3. For each iteration, the parent depth should be provided.

def countDepths(node, current_depth):
    if node is None: # 1
        return 0
    
    left_depth = countDepths(node.left, current_depth + 1) # 2
    right_depth = countDepths(node.right, current_depth + 1)
    return current_depth + left_depth + right_depth

def nodeDepths(root):
    # Write your code here.
    return countDepths(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

if __name__ == "__main__":
    print("Node Depths")

    # Build the tree
    root = BinaryTree(1, 
                      BinaryTree(2, 
                                 BinaryTree(4, 
                                            BinaryTree(8, None, None), BinaryTree(9, None, None)), 
                                 BinaryTree(5, None, None)), 
                      BinaryTree(3, 
                                 BinaryTree(6, None, None), 
                                 BinaryTree(7, None, None)))
    
    # Count the node depths
    result = nodeDepths(root)
    print(f"Total Node Depths: {result}")  # Expected output: 16