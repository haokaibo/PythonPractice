# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
1, 2, 3

1 left: None Right: 2, 3
2 left: 1 Right: 3
3 left: 1, 2

1, 2
1 left: None, Right: 2
2 left: 1 right: None

2, 3
2 left: None, right: 3
3 left: 2, right: None
'''


class UniqueBinaryTreeII:

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def helper(nums: range) -> List[TreeNode]:
            if nums is None or len(nums) == 0:
                return [None]
            roots = []
            for num in nums:
                index = nums.index(num)
                lefts = helper(nums[:index])
                rights = helper(nums[index+1:])
                for left in lefts:
                    for right in rights:
                        root = TreeNode(num)
                        root.left = left
                        root.right = right
                        roots.append(root)
            return roots

        return helper(range(1, n + 1))

    def iterate_tree_to_list(self, root):
        list = [root.name]

        def helper(root):
            if root is None:
                return
            else:
                if root.left is None and root.right is None:
                    return
                if root.left is None:
                    list.append(None)
                else: list.append(root.left.name)
                if root.right is None:
                    list.append(None)
                else: list.append(root.right.name)
                helper(root.left)
                helper(root.right)

        helper(root)
        return list


if __name__ == '__main__':
    uniqueBinaryTreeII = UniqueBinaryTreeII()
    trees = uniqueBinaryTreeII.generateTrees(3)
    print([uniqueBinaryTreeII.iterate_tree_to_list(tree) for tree in trees])
