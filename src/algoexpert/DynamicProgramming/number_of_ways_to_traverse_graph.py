"""
Number Of Ways To Traverse Graph

You're given the dimensions (width and height) of a rectangular grid. Write
a function that returns the number of different paths you can take to
traverse the grid from the top-left corner to the bottom-right corner,
assuming you can only move right or down at each step.
"""

"""_summary_
Solution(Time:O(w * h), Space: O(w * h) )
target: find the ways for left top -> right bottom
reach the end: height == 0 and right == 0
action: down(height-1), right(width-1)
1 1
1 2
1 3(1 + 2)
"""

class Solution:

    @staticmethod
    def numberOfWaysToTraverseGraph(width, height):
        # Write your code here.
        if width == 1 or height == 1:
            return 1
            
        matrix = [[1] * width] * height
        for r in range(1, height):
            for c in range(1, width):
                matrix[r][c] = matrix[r - 1][c] + matrix[r][c - 1]
        
        return matrix[height - 1][width - 1]

width = 2
height = 3
print(f"numberOfWaysToTraverseGraph for width: {width}, height: {height} -> "
       f"{Solution.numberOfWaysToTraverseGraph(width, height)}")