"""

Input:
      a0  2^(Depth) -1
   b1               c2   node index is 2^(Depth-1)+1 or 2^(Depth) -1
 d3   e4        f5    g6 0 or 2 ^ 2 -1
h7 i8 j9 k10        n13 o14 for last level return all the node without child

Output: [a b d h i j k l m n o g c]

question to ask: is the tree is a balanced binary tree
assumption: The input is not full balanced binary tree.
Solution:
Take top, left ,bottom, right lists to hold different nodes.
Traverse the tree by BFS.
Take a queue to hold the tree nodes for each level.
Build a new Node class which has the depth and sequence number.
build lists top, left, bottom, right to hold the result
iterate the queue, pop element and push its children, until to the end.

if the depth==0 then top.append
elif curr.seq is 2^curr.depth-1 then is the first element of the level, add to left list
elif curr.seq is 2^(curr.depth+1)-2 then is the last element of the level, insert to right list 0 index
elif curr.left is None and curr.right is None is the element in the bottom, add to bottom
return the result for top+ left + bottom + right
time: O(n)
space: O(n)
"""
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None, depth=0, seq=0):
        self.val = val
        self.left = left
        self.right = right
        self.depth = depth
        self.seq = seq

    def __str__(self):
        return f"val={self.val}, depth={self.depth}, seq={self.seq}"


class Solution:
    def __init__(self):
        pass

    def anti_clock_traverse_not_complete_tree(self, root):
        # edge case handling
        if root is None:
            return None

        left, right, bottom = [], [], []
        d = deque()
        d.append(Node(root.val, root.left, root.right))
        last_level = 0
        pre = None
        while len(d) != 0:
            curr = d.popleft()
            if pre is None or curr.depth - 1 == pre.depth:  # top or left
                left.append(curr.val)
                # check if the level is the last level
                if curr.left is None and curr.right is None:
                    last_level = curr.depth
                    # clean the bottom list, since previous bottom elements are not bottom elements.
                    bottom = []
            elif len(d) > 0 and curr.depth + 1 == d[0].depth:  # right
                right.insert(0, curr.val)
            elif curr.left is None and curr.right is None and last_level == curr.depth:
                # bottom and ensure the node not in the last level may not be added
                bottom.append(curr.val)

            # first node of the element of the level
            if curr.left is not None:
                d.append(Node(curr.left.val,
                              left=curr.left.left,
                              right=curr.left.right,
                              depth=curr.depth + 1,
                              seq=2 * curr.seq + 1))
            if curr.right is not None:
                d.append(Node(curr.right.val,
                              left=curr.right.left,
                              right=curr.right.right,
                              depth=curr.depth + 1,
                              seq=2 * curr.seq + 2))
            pre = curr
        # debug
        # print(f'left={left}, bottom={bottom}, right={right}')
        return left + bottom + right

'''
       a
    b       c
  d   e   f   g
 h i j k     n o
 
      [a  b c d e f g    h]
depth  0->1 1 2 2 2 2 -> 3
'''
root = Node('a',
            Node('b',
                 Node('d',
                      Node('h'),
                      Node('i')),
                 Node('e',
                      Node('j'),
                      Node('k'))),
            Node('c',
                 Node('f'),
                 Node('g',
                      Node('n'),
                      Node('o')))
            )
# s = Solution()
# result = s.anti_clock_traverse_not_complete_tree(root)
# print(result)

'''
input:
       a
    b       c
  d   e   f   g
     j k     n o
output: [a b d j k n o g c] = [a b d j] + [k n o] + [g c]
 
      [a  b c d e f g    j]
depth  0->1 1 2 2 2 2 -> 3
'''
root = Node('a',
            Node('b',
                 Node('d'),
                 Node('e',
                      Node('j'),
                      Node('k'))),
            Node('c',
                 Node('f'),
                 Node('g',
                      Node('n'),
                      Node('o')))
            )
s = Solution()
result = s.anti_clock_traverse_not_complete_tree(root)
print(result)

