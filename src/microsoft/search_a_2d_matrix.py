"""
LeetCode 74. Search a 2D Matrix [Medium]

Write an efficient algorithm that searches for a value target in an m x n
integer matrix. The matrix has the following properties:
  - Integers in each row are sorted in non-decreasing order (left to right).
  - The first integer of each row is greater than the last integer of the
    previous row.

Example 1:
Input:  matrix = [[1, 3, 5, 7],
                  [10,11,16,20],
                  [23,30,34,60]], target = 3
Output: True

Example 2:
Input:  matrix = [[1, 3, 5, 7],
                  [10,11,16,20],
                  [23,30,34,60]], target = 13
Output: False

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

Solution (treating the matrix as a single sorted 1D array):

Because each row is sorted and the first element of every row is greater
than the last element of the previous row, the matrix is globally ordered
in row-major order. So we can binary-search index `mid` over the virtual
range [0, m*n), and map it back to (row, col) = (mid // n, mid % n).

Time : O(log(m * n))
Space: O(1)

Note: This problem differs from LeetCode 240 (Search a 2D Matrix II), where
each row and each column is sorted but the row-starts are not necessarily
greater than the previous row-end. That variant requires a staircase search.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            r = mid // n
            c = mid % n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
        
        
if __name__ == "__main__":
    cases = [
        # ((matrix, target), expected)
        ((([[1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]], 3),  True)),
        ((([[1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]], 13), False)),
        ((([[1]],                    1),  True)),
        ((([[1]],                    0),  False)),
        ((([[1, 3]],                 3),  True)),  # 1x2, original test
        ((([[1, 3]],                 2),  False)),
        ((([[1, 3, 5]],              5),  True)),  # last element
        ((([[1, 3, 5]],              0),  False)), # below range
        ((([[1, 3, 5]],              6),  False)), # above range
    ]
    for case in cases:
        matrix, target = case[0]
        result = Solution().searchMatrix(matrix, target)
        msg = "OK" if result == case[1] else "Failed"
        print(f"{msg} searchMatrix(target={target}) = {result} (expected {case[1]})")