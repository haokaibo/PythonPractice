"""
LeetCode 48 - Rotate Image
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/

Problem:
    You are given an n x n square matrix (list of lists) representing an image,
    rotate the image by 90 degrees (clockwise) in place, i.e. modify the input
    2D matrix directly. Do NOT allocate another 2D matrix.

    After rotation, the element originally at (row, col) moves to (col, n-1-row).

Example:
    Input:  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[16,14,4,1],[12,6,8,9],[16,7,10,11]]

Intuition:
    A 90° clockwise rotation cycles four cells per position:
        top <- left <- bottom <- right <- top
    We process the matrix ring by ring from the outside in. For each ring
    defined by `begin` (top-left) and `end` (bottom-right), iterating the
    offset `k = j - begin` over `range(begin, end)`, the four cells are:
        top    = (begin, j)
        right  = (j, end)
        bottom = (end, end - k)
        left   = (end - k, begin)

Complexity:
    Time:  O(n^2)  -- every cell is touched exactly once.
    Space: O(1)    -- in-place, only a single temp variable per swap.
"""
class Solution(object):
    def rotate(self, matrix):
        """
        Rotate the n x n matrix 90 degrees clockwise, in place.

        :type matrix: List[List[int]]
        :rtype: None  Modify matrix in-place instead.
        """
        if not matrix:
            return
        
        begin, end = 0, len(matrix) - 1

        while begin < end:
            for j in range(begin, end):
                # offset of this element within the current layer
                offset = j - begin

                # 90 clockwise: top <- left <- bottom <- right <- top
                #   top    = (begin, j)
                #   left   = (end - offset, begin)
                #   bottom = (end, end - offset)
                #   right  = (j, end)
                temp = matrix[begin][j]
                matrix[begin][j] = matrix[end - offset][begin]
                matrix[end - offset][begin] = matrix[end][end - offset]
                matrix[end][end - offset] = matrix[j][end]
                matrix[j][end] = temp

            begin += 1
            end -= 1
    
                
def _expected(matrix):
    """Reference 90 clockwise rotation (out of place) to validate against."""
    n = len(matrix)
    return [[matrix[n - 1 - c][r] for c in range(n)] for r in range(n)]


def _run(name, matrix):
    original = [row[:] for row in matrix]
    Solution().rotate(matrix)
    ok = matrix == _expected(original)
    print(f"{name}: {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("  got     :", matrix)
        print("  expected:", _expected(original))


if __name__ == "__main__":
    # 1x1
    _run("1x1", [[1]])
    # 2x2
    _run("2x2", [[1, 2], [3, 4]])
    # 3x3 (odd -> has a fixed center)
    _run("3x3", [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # 4x4 (even)
    _run("4x4", [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
    # 5x5 (odd, multiple rings -> stress test for inner-layer indexing)
    _run("5x5", [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25]])