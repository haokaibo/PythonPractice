"""
Given a number n which will be used to created a n x n matrix. Place the n queens in the matrix.
And make sure all the queens will not threat each other. Return the n queens positions(Tuple).
x

xx
xx

xxx
xxx
xxx

x0xx
xxx0
0xxx
xx0x
"""

from collections import deque


class NQueens:
    def __init__(self, n):
        if n is None or n <= 0:
            raise ValueError(f'Parameter "n" should not be "{n}", "n" should be an integer which is greater than 0.')
        self.cols = self.rows = n
        self.matrix = [[0 for i in range(n)] for j in range(n)]
        self.queens = deque()

    def safe(self, row, col):
        for i in range(len(self.queens) - 1):
            if row == self.queens[i][0] or col == self.queens[i][1] \
                    or abs(row - self.queens[i][0]) == abs(col - self.queens[i][1]):
                return False

        return True

    def place_queen(self, col):
        if col < self.cols:
            row = 0
            while row < self.rows:
                self.queens.append((row, col))
                if self.safe(row, col) and self.place_queen(col + 1):
                    return True
                self.queens.pop()
                row += 1
            # if there is no suitable queen in each row.
            if row == self.rows:
                return False
        return True

    def get_queens(self):
        self.place_queen(0)
        if len(self.queens) == 0:
            return None
        else:
            return list(self.queens)


for i in range(1, 6):
    nq = NQueens(i)
    print(f'N={i}, {nq.get_queens()}')
