# This is an input class. Do not edit.
"""
Solution(Time: O(n), Space: O(d), the depth of the tree)
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBstHelper(tree, minValue, maxValue):
    """
    For each tree node it should greater than a value (e.g. left node , the minValue is float("-inf"), the max value is the parent value)
    """
    # Child of leaf node or the single node tree
    if tree is None:
        return True

    if tree.value < minValue or tree.value >= maxValue:
        return False

    isLeftValid = validateBstHelper(tree.left, minValue, tree.value)
    isRightValid = validateBstHelper(tree.right, tree.value, maxValue)

    return isLeftValid and isRightValid

def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float("-inf"), float("inf"))

nodes = [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": None, "right": "22", "value": 15},
      {"id": "22", "left": None, "right": None, "value": 22},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": None, "right": "11", "value": 5},
      {"id": "11", "left": None, "right": None, "value": 11},
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

print(f"validateBst = {validateBst(node_dict['10'])}")


