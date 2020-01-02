# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class IsBST:

    def isValidBST(self, root: TreeNode) -> bool:
        def check_left(root: TreeNode, root_value: int):
            if root is None:
                return True

            if root.left is not None:
                if root.left.val >= root.val:
                    return False
                if root_value is not None and root.left.val >= root_value:
                    return False
                if not check_left(root.left, root_value):
                    return False
            if root.right is not None:
                if root.right.val <= root.val:
                    return False
                if root_value is not None and root.right.val >= root_value:
                    return False
                if not check_right(root.right, root_value):
                    return False
            return True

        def check_right(root: TreeNode, root_value: int):
            if root is None:
                return True

            if root.left is not None:
                if root.left.val >= root.val:
                    return False
                if root_value is not None and root.left.val <= root_value:
                    return False
                if not check_left(root.left, root_value):
                    return False
            if root.right is not None:
                if root.right.val <= root.val:
                    return False
                if root_value is not None and root.right.val <= root_value:
                    return False
                if not check_right(root.right, root_value):
                    return False
            return True

        return check_left(root, root.val) and check_right(root, root.val)

    def buildTree(self, nums):
        if nums is None or len(nums) == 0:
            return None

        begin = level = 0
        nodes = []
        root = None
        while begin < len(nums):
            end = min(begin + pow(2, level), len(nums))
            for i in range(begin, end):
                if nums[i] is None:
                    continue
                node = TreeNode(nums[i])
                nodes.append(node)
                if root is None:
                    root = node
                elif i % 2 != 0:
                    nodes[(i-1) // 2].left = node
                else:
                    nodes[(i-1) // 2].right = node
            level += 1
            begin = end
        return root


if __name__ == '__main__':
    values = [3, 1, 5, 0, 2, 4, 6, None, None, None, 3]
    exec = IsBST()
    root = exec.buildTree(values)

    assert not exec.isValidBST(root)
