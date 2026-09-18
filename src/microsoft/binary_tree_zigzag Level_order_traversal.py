"""
Binary Tree Zigzag Level Order Traversal (LeetCode 103)

Given the root of a binary tree, return the zigzag level order traversal of its
nodes' values. (i.e., from left to right, then right to left for the next level
and alternate between).

Example:
    Input:  root = [3,9,20,null,null,15,7]
    Output: [[3],[20,9],[15,7]]

    Explanation:
        Level 0: 3                       (left -> right)
        Level 1: 20 -> 9                  (right -> left, i.e. reversed)
        Level 2: 15 -> 7                  (left -> right)

    3
   / \
  9  20
    /  \
   15   7

Intuition:
A standard BFS level-order traversal visits each level left-to-right. To get the
zigzag pattern we simply reverse the collected values of every odd level. We use
a deque/queue: enqueue the root, then for each level pop all current nodes (in
left->right order), push their values, enqueue their children, and reverse the
level list when the level index is odd. (Equivalently, alternate the append
direction: use appendleft on odd levels.)

Time: O(n), Space: O(n)
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        BFS with a queue. For each level, collect node values in traversal order
        and reverse the list on odd levels (0-indexed) to produce the zigzag.
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                current_level.reverse()

            result.append(current_level)
            level += 1

        return result


if __name__ == "__main__":
    # Build the example tree: 3 / 9 20 / null null 15 7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))  # [[3], [20, 9], [15, 7]]
