"""

Input:
      a0  2^(Depth) -1
   b1      c2   node index is 2^(Depth-1)+1 or 2^(Depth) -1
 d3   e4   f5  g6 0 or 2 ^ 2 -1
h7 i j k l m n o for last level return all the node without child

Output: [a b d h i j k l m n o g c]

assumption: The input is balanced binary tree.
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
from queue import Queue


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

    def anti_clock_traverse_tree(self, root):
        # edge case handling
        if root is None:
            return None

        top, left, right, bottom = [], [], [], []
        q = Queue()

        q.put(Node(root.val, root.left, root.right))
        while not q.empty():
            curr = q.get()
            if curr.depth == 0:  # top
                top.append(curr.val)
            elif curr.seq == 2 ** curr.depth - 1:  # left
                left.append(curr.val)
            elif curr.seq == 2 ** (curr.depth + 1) - 2:  # right
                right.insert(0, curr.val)
            elif curr.left is None and curr.right is None: # bottom
                bottom.append(curr.val)

            # first node of the element of the level
            if curr.left is not None:
                q.put(Node(curr.left.val,
                           left=curr.left.left,
                           right=curr.left.right,
                           depth=curr.depth + 1,
                           seq=2 * curr.seq + 1))
            if curr.right is not None:
                q.put(Node(curr.right.val,
                           left=curr.right.left,
                           right=curr.right.right,
                           depth=curr.depth + 1,
                           seq=2 * curr.seq + 2))

        return top + left + bottom + right


root = Node('a',
            Node('b',
                 Node('d',
                      Node('h'),
                      Node('i')),
                 Node('e',
                      Node('j'),
                      Node('k'))),
            Node('c',
                 Node('f',
                      Node('l'),
                      Node('m')),
                 Node('g',
                      Node('n'),
                      Node('o')))
            )
s = Solution()
result = s.anti_clock_traverse_tree(root)
print(result)
