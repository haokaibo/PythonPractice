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

