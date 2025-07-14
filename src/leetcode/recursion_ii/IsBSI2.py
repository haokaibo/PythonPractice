""" Program to check if a given Binary
Tree is balanced like a Red-Black Tree """


# Helper function that allocates a new
# node with the given data and None
# left and right poers.
class TreeNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Returns true if given tree is BST.
def isBST(root, l=None, r=None):
    # Base condition
    if (root == None):
        return True

    # if left node exist then check it has
    # correct data or not i.e. left node's data
    # should be less than root's data
    if (l != None and root.data <= l.data):
        return False

    # if right node exist then check it has
    # correct data or not i.e. right node's data
    # should be greater than root's data
    if (r != None and root.data >= r.data):
        return False

    # check recursively for every node.
    return isBST(root.left, l, root) and \
           isBST(root.right, root, r)


# Driver Code
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    root.left.right.right = TreeNode(3)
    if (isBST(root, None, None)):
        print("Is BST")
    else:
        print("Not a BST")

    # This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
