"""
Depth First Search

You're given a Node class that has a "name" property and an array of
pointers to child nodes. The DFS traversal of a graph produces a value by
visiting nodes in a depth-first manner.

Starting at the root node of a graph, the main principle behind depth-first
search traversal is to keep on going deep into the graph until you hit a
node that has no more children. By then, you backtrack and continue down the
most recently found path. You keep doing this until you've visited all of
the nodes.

To do this, of course, you have to keep track of every node you've visited.
The order in which you visit the nodes will eventually be returned as an
array of node values in the order in which they were visited.
"""

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Solution
    # An array is provided for the holding the nodes to be iterated.
    # The depth first search should iterate the left node before the right node. 
    # The recursion should stop iteration when it is a leaf node
    # then continue to iterate the next child node part if there is any.
    # Time complexity: O(n)
    # Space complexity: O(n)
    def depthFirstSearch(self, array):
        # Write your code here.
        # 1. append the current node name in the array
        array.append(self.name)

        # 2. check the children
        if self.children is not None and len(self.children) > 0:
            for child in self.children:
                child.depthFirstSearch(array)
        return array

