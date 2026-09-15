"""
Set Matrix Zeroes (LeetCode 73)

Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.
You must do it in-place.

Example:
    Input:  [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    Output: [[0,0,0,0],[0,0,7,0],[0,0,11,0],[0,0,15,0]]

Intuition:
Iterate each cell in the matrix. If a cell is 0, log the row in a num (e.g. 101) for the zero row.
Log the col in a num for the zero col.
Iterate the row and col numbers for setting the zeros.

Time: O(m*n), Space: O(1)
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = 0
        cols = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows |= (1 << i)
                    cols |= (1 << j)
                    
        for k in range(len(matrix)):
            for l in range(len(matrix[k])):
                if (1 << k) & rows or (1 << l) & cols:
                    matrix[k][l] = 0
                    
        return matrix
                

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    print(Solution().setZeroes(matrix=matrix))
