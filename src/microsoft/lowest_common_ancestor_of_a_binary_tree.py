# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Solution:
1. Recursively traverse the tree (post-order DFS).
2. If the current node is None, return None.
3. If the current node is either p or q, return the current node — it is a candidate ancestor.
4. Recursively search the left and right subtrees.
5. If both left and right return non-None, the current node is the LCA (p and q are in different subtrees).
6. If only one side returns non-None, that side propagates up the single match.

Time: O(n)  — every node is visited exactly once.
Space: O(h) — recursion stack depth, where h is the height of the tree.
              In the worst case (skewed tree) h = n → O(n);
              in a balanced tree h = log(n) → O(log n).
"""
class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base case: empty subtree or found one of the targets
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Both subtrees contain a target → current node is the LCA
        if left and right:
            return root

        # Otherwise return whichever side is non-None (or None)
        return left if left else right
