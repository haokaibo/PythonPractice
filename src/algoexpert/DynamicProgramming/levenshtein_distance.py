"""
Levenshtein Distance

You're given two strings. Write a function that returns the edit distance
between the two strings.

The edit distance between two strings can be calculated by determining the
minimum number of edits required to transform one string into the other.
The allowed edits are: inserting a character into a string, deleting a
character from a string, or replacing a character in a string with another
character.
"""

"""
Solution
1. Build a matrix to holder the chars from the horizontal and vertical respectively.
2. Calculate the operations for each combination for each cell in the matrix.

if the str2[col] == str1[row]:
    matrix[row][col] = matrix[row - 1][col - 1]
else:
    matrix[row][col] = 1 + min(matrix[row - 1][col], matrix[row][col - 1], matrix[row - 1][col - 1])

e.g. 
""ya vs ""a

   ""   y   a   b   d
""  0   1   2   3   4
a   1   1   1   2   3
b   2   2   2   1   2
c   3   3   3   2   2
"""
class Solution:
    @staticmethod
    def levenshteinDistance(str1, str2):
        rows = len(str1) + 1
        cols = len(str2) + 1
        matrix = [[r + c for c in range(cols)] for r in range(rows)]

        for r in range(1, rows):
            for c in range(1, cols):
                if str1[r-1] == str2[c-1]:
                    matrix[r][c] = matrix[r-1][c-1]
                else:
                    matrix[r][c] = 1 + min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])

        return matrix[rows-1][cols-1]

print(f"levenshteinDistance: {Solution.levenshteinDistance('abc','fabd')}")