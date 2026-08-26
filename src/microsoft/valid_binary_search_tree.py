"""
LeetCode 98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search
tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the
  node's key.
- The right subtree of a node contains only nodes with keys greater than the
  node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
"""

"""
Solution:
1. Recursively validate each subtree within an (open, close) value bound
2. Left child must be within (-inf, node.val), right child within (node.val, +inf)
Time: O(n), Space: O(h) where h is the tree height (recursion stack)
"""
import math

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, low, high):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, -math.inf, math.inf)
