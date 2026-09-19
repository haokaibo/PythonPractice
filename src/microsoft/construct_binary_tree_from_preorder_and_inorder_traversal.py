# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Solution:
1. The first element of preorder traversal is always the root of the (sub)tree.
2. Locate that root in the inorder traversal — elements to the left belong to the left subtree,
   elements to the right belong to the right subtree.
3. Recursively apply the same logic: pop the next root from preorder, split the inorder range,
   and build left subtree first (preorder order is root → left → right).

Time: O(n) — each node is visited once; the inorder hash map allows O(1) root lookups.
Space: O(n) — the hash map + recursion stack (O(h), where h is the height of the tree).
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Build a hash map to map value -> index in inorder array for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None

            # Pick current root from preorder traversal
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # Split point in inorder traversal
            inorder_pivot = inorder_map[root_val]

            # Build left and right subtrees
            # Must build left subtree first because preorder visits root -> left -> right
            root.left = helper(left_idx, inorder_pivot - 1)
            root.right = helper(inorder_pivot + 1, right_idx)

            return root

        return helper(0, len(inorder) - 1)
