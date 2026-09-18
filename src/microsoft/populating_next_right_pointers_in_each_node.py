"""
Populating Next Right Pointers in Each Node (LeetCode 116)

Given the root of a perfect binary tree, connect each node to its next right
node. If there is no next right node, the next pointer should be set to null.

A *perfect* binary tree is one where every level (except possibly the last)
is completely filled, and all nodes in the last level are as far left as
possible. The tree contains between 1 and 2^12 - 1 nodes.

Initially, every `next` pointer is null. After connecting, each node's `next`
should point to the node immediately to its right on the same level; the
rightmost node on each level points to null.

Example:
    Input: root = [1,2,3,4,5,6,7]
    Output: [1,#,2,#,3,#,4,#,5,#,6,#,7,#]
    (The '#' marks the end of each level, i.e. where next becomes null.)

    Explanation:
        1              ->  1 -> null
       / \\
      2   3            ->  2 -> 3 -> null
     / \\ / \\
    4  5 6  7          ->  4 -> 5 -> 6 -> 7 -> null

    The serialization of the output uses level order with '#' separators,
    where each '#' indicates that the next pointer of the preceding node is
    null (end of that level).

Intuition:
In a *perfect* binary tree every parent has exactly two children, and the
"next" relationship can be built using only the already-established `next`
links of the parent level -- yielding an O(1) extra-space solution.

There are two relationships to wire:
1. Parent link:      leftChild.next  = rightChild      (same parent)
2. Cross-parent link: rightChild.next = parent.next.left
   (the rightmost child of one parent connects to the leftmost child of the
   next parent on the same level, reachable via the parent's already-built
   `next` pointer.)

A recursive form wires (1) and (2) top-down, then recurses into the children.
Because each recursion descends one tree level and the tree is perfect, the
recursion depth equals the tree height h = log2(n+1), so the call stack uses
O(log n) space. An iterative level-by-level version that walks a whole level
via `next` pointers and wires the children below achieves O(1) extra space.

Time:  O(n) - every node is visited exactly once.
Space: O(log n) for the recursion stack (tree height).
       O(1) is achievable with an iterative, next-pointer-only traversal.
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        Populate each node's `next` pointer so it points to its next right
        node, using the recursive top-down approach on a perfect tree.

        :type root: Node
        :rtype: Node
        :return: The root of the tree with `next` pointers wired level by level.

        Algorithm:
            For every non-leaf node we establish two links:
              (1) left.next = right            -- same parent, adjacent children
              (2) right.next = root.next.left   -- cross-parent link, available
                                                  because root.next is already
                                                  wired at this level.
            The root of the current subtree always has its `next` correctly set
            (null for the true root), so recursing on root.left and root.right is
            safe and preserves the invariant.

        Time:  O(n) - each node is visited once.
        Space: O(log n) - recursion stack depth equals the tree height.
        """
        if not root or not root.left:
            return root

        # 1. Connect the two children of the same parent.
        root.left.next = root.right

        # 2. Connect across parents using the parent's already-built `next`.
        if root.next:
            root.right.next = root.next.left

        # Recurse into the subtrees (their roots inherit the correct `next`).
        self.connect(root.left)
        self.connect(root.right)

        return root
