
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Solution:
1. Iterate the tree recursively to ensure the left node is less than current and the right is greater than current
2. Both the left and right sub tree is valid bst
Time: O(n), Space: O(1)
"""
class Solution(object):
    
    def validateBstHelper(self, tree, minValue=float('-inf'), maxValue=float('inf')):
        """
        For each tree node it should greater than a value (e.g. left node , the minValue is float("-inf"), the max value is the parent value)
        """
        # Child of leaf node or the single node tree
        if tree is None:
            return True

        if tree.val <= minValue or tree.val >= maxValue:
            return False

        isLeftValid = self.validateBstHelper(tree.left, minValue, tree.val)
        isRightValid = self.validateBstHelper(tree.right, tree.val, maxValue)

        return isLeftValid and isRightValid
        
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validateBstHelper(root)
        
        