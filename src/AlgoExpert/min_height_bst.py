"""
Solution(Time: O(n), Space: O(n))
The min height means the BST is a well balanced tree. 
The medium item in the sorted array should be the root.
e.g. [1, 2, 5, 7, 10, 13, 14, 15, 22]
mediumIndex = (begin + end) // 2 = (0 + 8) // 2 = 4
Then its left is the element (begin + mediumIndex - 1) // 2 = (0 + 4 - 1) // 2 = 1
right is the element (mediumIndex + 1 + end) // 2 = (4 + 1 + 8) // 2 = 6
Do this recursively.
"""

def minHeightBst(array):
    
    return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, begin, end):
    if begin > end:
        return None
    mediumIndex = (end + begin) // 2
    root = BST(array[mediumIndex])
    root.left = minHeightBstHelper(array, begin, mediumIndex - 1)
    root.right = minHeightBstHelper(array, mediumIndex + 1, end)
    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
