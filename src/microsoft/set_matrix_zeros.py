"""
Intuition:
Iterate each cell in the matrix. if a cell is 0, log the row in a num(e.g. 101) for the zero row. Log the col in a num for the zero col.
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
            hasZero = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if not hasZero:
                        rows += i + 1
                        hasZero = True
                    cols += j + 1
                    
        for k in range(len(matrix)):
            for l in range(len(matrix[k])):
                if (k + 1) & rows == k + 1 or (l + 1) & cols == l + 1:
                    matrix[k][l] = 0
                    
        return matrix
                

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
    print(Solution().setZeroes(matrix=matrix))