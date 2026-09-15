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

    def setZeroesOptimized(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # 用第一行和第一列标记其余位置的 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据标记将对应元素置 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 最后处理第一行和第一列
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix

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
    print(f"Solution().setZeroes(matrix=matrix) = {Solution().setZeroes(matrix=matrix)}")
    matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    print(f"Solution().setZeroesOptimized(matrix=matrix) = {Solution().setZeroesOptimized(matrix=matrix)}")
