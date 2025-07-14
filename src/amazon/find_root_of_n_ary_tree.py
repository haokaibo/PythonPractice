"""
Given all the nodes of an N-ary tree as an array Node[] tree
where each node has a unique value.
Find and return the root of the N-ary tree
        1
      / | \
     2  3  4
    / \
   5  6
solution:
push all the node and its child nodes to different dict respectively,
iterate the node array from begin to end.
if there child node val in the parent dict just remove parent node in the parent dict.
check if there is a node left in the parent dict.


Time: O(linear)
Space: O(n + n * N) : N is the child node count
"""


class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children

    def __str__(self):
        return str(self.val)


def find_root(tree: [Node]):
    if tree is None or len(tree) == 0:
        return None
    else:
        parents = dict()
        children = dict()
        for node in tree:
            parents[node.val] = node
            if node.children is not None:
                for child in node.children:
                    children[child.val] = child
                    if child.val in parents:
                        del parents[child.val]
    if len(parents) > 0:
        return next(iter(parents.values()))
    return None


"""
Time: O(linear)
Space:O(1)
"""


def find_root_for_better_space_complexity(tree: [Node]):
    if tree is None or len(tree) == 0:
        return None
    else:
        sum = 0
        for node in tree:
            sum += node.val
            if node.children is not None:
                for child in node.children:
                    sum -= child.val
    if sum > 0:
        return Node(sum)
    return None


"""
        1
      / | \
     2  3  4
    / \
   5  6
"""
tree = [Node(1, [Node(2), Node(3), Node(4)]),
        Node(2, [Node(5), Node(6)]),
        Node(3),
        Node(4),
        Node(5),
        Node(6)]
root = find_root(tree)
print(root)
root = find_root_for_better_space_complexity(tree)
print(root)
