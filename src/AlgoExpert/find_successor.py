# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

"""
Solution(Time: O(n), Space: O(h)), h is the height of the tree.
Explore the scenarios.
If the node is the top node
| Node    | Successor | Description |
| --------| --------- | ----------- |
| 1       | 3         | root -> right child / None       |
| 2       | 5         | left branch has right child  -> right child  |
| 4       | 2         | left branch has no right child but parent -> parent|
| 6       | 4         | left leaf node -> parent|
| 5       | 1         | right leaf node has no child -> parent.parent |


6 - > 4 -> 2 -> 5 -> 1 -> 3

"""
class NodeInfo:
    def __init__(self, found, successor):
        self.found = found
        self.successor = successor
        
def findSuccessorHelper(tree, node):
     # None check
    if tree is None:
        return None

    # Found the node
    if node == tree.value:
        # Get the successor
        if tree.right is None:
            if tree.parent and tree.parent.left and tree.parent.left.value == tree.value:
                return tree.parent
            elif tree.parent and tree.parent.right and tree.parent.right.value == tree.value:
                return tree.parent.parent
        else:
            return tree.right

    leftResult = findSuccessorHelper(tree.left, node)
    if leftResult is not None:
        return leftResult
    
    rightResult = findSuccessorHelper(tree.right, node)
    return rightResult
    
def findSuccessor(tree, node):
    result = findSuccessorHelper(tree, node)
    if result is None:
        return result
    else:
        return result.value
    
nodes = [
      {"id": "1", "left": "2", "parent": None, "right": "3", "value": 1},
      {"id": "2", "left": "4", "parent": "1", "right": "5", "value": 2},
      {"id": "3", "left": None, "parent": "1", "right": None, "value": 3},
      {"id": "4", "left": "6", "parent": "2", "right": None, "value": 4},
      {"id": "5", "left": None, "parent": "2", "right": None, "value": 5},
      {"id": "6", "left": None, "parent": "4", "right": None, "value": 6}
    ]
node_map = {}
for node in nodes[::-1]:
    id = node["id"]
    node_map[id] = BinaryTree(node["value"], None, None, None)

for node in nodes:
    id = node["id"]
    left = node_map.get(node["left"], None)
    right = node_map.get(node["right"], None)
    parent = node_map.get(node["parent"], None)
    node_map[id].left = left
    node_map[id].right = right
    node_map[id].parent = parent

print(f"findSuccessor(node_map['1'], 5) = {findSuccessor(node_map['1'], 5)}")  # 1
print(f"findSuccessor(node_map['1'], 2) = {findSuccessor(node_map['1'], 2)}")  # 5
print(f"findSuccessor(node_map['1'], 3) = {findSuccessor(node_map['1'], 3)}")  # None
print(f"findSuccessor(node_map['1'], 4) = {findSuccessor(node_map['1'], 4)}") #2