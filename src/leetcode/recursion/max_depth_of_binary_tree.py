# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MaxDepthOfBinaryTree:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        max_depth = max((left_max_depth, right_max_depth)) + 1
        return max_depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert 3 == MaxDepthOfBinaryTree().maxDepth(root)
