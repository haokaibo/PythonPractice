# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    """
    Solution(Average Time: O(log(n)), Space: O(1), Worst: O(n), Space: O(1))
    1. Single node BST. - The verification is that it has no child. Add a level for checking if this is the first level of the tree. 
    2. Impelement a search function to find the cloest node.
    3. Insert, contains and remove function use the search function for position finding.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def searchParent(self, value, parent=None):
        if self.value < value:
            return self.right.searchParent(value, self)
        elif self.value > value:
            return self.left.searchParent(value, self)
        else:
            return parent
            
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        current = self
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                current = current.left
            elif value >= current.value:
                if current.right is None:
                    current.right = BST(value)
                    break
                current = current.right

        return self
                

    
    def contains(self, value):
        if self.value < value:
            return self.right.contains(value) if self.right is not None else False
        elif self.value > value:
            return self.left.contains(value) if self.left is not None else False
        else:
            return True


    def remove(self, value, parent=None):
        # 1. find the the node 
        current = self
        while current is not None:
            if current.value == value:
                break
            elif current.value < value:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        # 2. not found
        if current is None:
            return self

        # 3. check if it is the root
        if parent == None:
            if current.left is None and current.right is None:
                return self
            elif current.left is not None and current.right is not None:
                current.value = current.right.getMinValue()
                current.right.remove(current.value, current)
            elif current.left is None:
                current.value = current.right.value
                current.left = current.right.left
                current.right = current.right.right
            elif current.right is None:
                current.value = current.left.value
                current.right = current.left.right
                current.left = current.left.left
                
            
        else:
            # leaf node
            if current.left is None and current.right is None:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            # Branch node
            elif current.left is not None and current.right is not None:
                current.value = current.right.getMinValue()
                current.right.remove(current.value, current)
            elif parent.right == current:
                parent.right = current.right if current.right is not None else current.left
            elif parent.left == current:
                parent.left = current.right if current.right is not None else current.left
                
    def getMinValue(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.value
        

def printNode(node):
    nodes = [node]

    while len(nodes) > 0:
        size = len(nodes)
        levelNodes = []
        for i in range(0, size):
            levelNodes.append(nodes[i].value)
            
            if nodes[i].left is not None:
                nodes.append(nodes[i].left)
            if nodes[i].right is not None:
                nodes.append(nodes[i].right)
        print(*levelNodes, sep=" ")
        # print("\n")
        nodes = nodes[size:]
nodes = [
        {"id": "10", "left": "5", "right": "15", "value": 10},
        {"id": "15", "left": "13", "right": "22", "value": 15},
        {"id": "22", "left": None, "right": None, "value": 22},
        {"id": "13", "left": "12", "right": "14", "value": 13},
        {"id": "14", "left": None, "right": None, "value": 14},
        {"id": "12", "left": None, "right": None, "value": 12},
        {"id": "5", "left": "2", "right": "5-2", "value": 5},
        {"id": "5-2", "left": None, "right": None, "value": 5},
        {"id": "2", "left": "1", "right": None, "value": 2},
        {"id": "1", "left": None, "right": None, "value": 1}
      ]
node_dict = dict()
for node in nodes[::-1]:
    left = None if node["left"] is None else node_dict[node["left"]]
    right = None if node["right"] is None else node_dict[node["right"]]
    id = node["id"]
    node_dict[id] = BST(node["value"])
    node_dict[id].left = left
    node_dict[id].right = right

print(node_dict["10"].value)

node_dict["10"].remove(10)



print(f"-"*5)
printNode(node_dict["10"])

# nodes = [
#         {"id": "10", "left": "5", "right": "15", "value": 10},
#         {"id": "15", "left": None, "right": None, "value": 15},
#         {"id": "5", "left": None, "right": None, "value": 5}
#       ]
# node_dict = dict()
# for node in nodes[::-1]:
#     left = None if node["left"] is None else node_dict[node["left"]]
#     right = None if node["right"] is None else node_dict[node["right"]]
#     id = node["id"]
#     node_dict[id] = BST(node["value"])
#     node_dict[id].left = left
#     node_dict[id].right = right

# printNode(node_dict["10"])
# print(node_dict["10"].contains(1))