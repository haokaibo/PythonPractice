"""
LeetCode 54. Spiral Matrix

Given an m x n matrix, return all the elements of the matrix in spiral
order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

"""
1. Use 2 dimension array to hold the numbers with an extra border
2. Right, Down, Left, Up functions to simulate the moves
Time: O(m*n), Space: O(m*n)
"""
class Solution(object):
  
    def is_complete(self, iterated, matrix):
        return len(iterated) == len(matrix) * len(matrix[0])


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        iterated = []
        
        left_border = -1
        upper_border = - 1
        m = len(matrix[0])
        n = len(matrix)
        right_border = m
        bottom_border = n
        x, y = 0, 0
        
        while len(iterated) < m * n:
            # move right
            while y < right_border:
                iterated.append(matrix[x][y])
                y += 1
                
            if self.is_complete(iterated, matrix):
                break

            upper_border += 1
            y -= 1
            x += 1
            
            

            # move down
            while x < bottom_border:
                iterated.append(matrix[x][y])
                x += 1

            if self.is_complete(iterated, matrix):
                break

            right_border -= 1
            x -= 1
            y -= 1
            

            
            # move left
            
            while y > left_border:
                iterated.append(matrix[x][y])
                y -= 1
                
            if self.is_complete(iterated, matrix):
                break
            bottom_border -= 1
            y += 1
            x -= 1
            
            # move up
            
            while x > upper_border:
                iterated.append(matrix[x][y])
                x -= 1
                
            if self.is_complete(iterated, matrix):
                break
            left_border += 1
            x += 1
            y += 1
            
        return iterated

if __name__ == "__main__":
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))