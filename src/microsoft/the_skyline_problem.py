"""
Solution:
1. Build a binary tree to hold the coordinates. The value is (x, y)
2. For each insertion of (x1, y), 
    if the node x1 is inserted as left node
        if the y < parent.y
            result.append((parent.x, y))
        else:
            result.append(x1, y)
    if the node x1 is inserted as right node
        result.append(parent.x, 0)
        result.append(x1, y)


Time: O(len(buildings)), Space: O(len(buildings))
"""

class Node(object):
    def __init__(self, x, y, parent = None, isLeft = False):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.parent = parent
        self.isLeft = isLeft

    def insert(self, x, y):
        current = self
        parent = self.parent
        isLeft = False
        while current:
            if x < current.x:
                parent = current
                current = current.left
                isLeft = True
            else:
                parent = current
                current = current.right
                isLeft = False

        node = None
        if parent:
            if isLeft:
                node = Node(x, y, parent, isLeft)
                parent.left = node
            else:
                node = Node(x, y, parent, isLeft) 
                parent.right = node

        return node


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        if not buildings or len(buildings) == 0:
            return result
        
        """
        Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8], [inf, inf, 0]]
        Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        """
        root = None
        for b in buildings:
            x1, x2, y = b[0], b[1], b[2]
            node = None
            if root is None:
                root = Node(x1, y, None)
                result.append([x1, y])
            else:
                node = root.insert(x1, y)
            
            if node:
                if node.parent:
                    if node.isLeft: 
                        if node.y > node.parent.y:
                            result.append([node.x, node.y])
                        else:
                            result.append([node.parent.x, node.y])
                    else:
                        result.append([node.parent.x, 0])
                        result.append([node.x, node.y])

            if root:
                root.insert(x2, y)

        last = buildings[-1]
        result.append([last[1], 0])
            
        return result