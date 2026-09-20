"""
LeetCode 200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n binary grid grid of '1's (land) and '0's (water), return the
number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. It is assumed that all four edges of the grid are
surrounded by water.

Example 1:
    Input:  grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
    ]
    Output: 1

Example 2:
    Input:  grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]
    Output: 3

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Out of bounds or water ('0') → stop exploring this branch.
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return

            # Sink the island: mark the current land as visited by overwriting
            # it with '0' instead of using a separate visited set.
            grid[r][c] = '0'

            # Recurse in all four cardinal directions.
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # Start of a new island — sink the whole connected component.
                    count += 1
                    dfs(i, j)

        return count


"""
Solution:
1. Scan the grid cell by cell. Each time an unvisited land cell ('1') is found,
   increment the island counter and launch a DFS to flood-fill the entire
   connected landmass.
2. DFS visits a cell, marks it as water ('0') in place to record the visit
   (this is the "sink the island" trick — no extra visited data structure),
   then recurses into the four cardinal neighbors.
3. After the DFS completes, the whole connected component is marked as
   visited, so it is never counted again.

Time:  O(m × n) — every cell is visited at most once; the DFS touches each
      land cell exactly once before sinking it.
Space: O(m × n) in the worst case — for an all-land grid the recursion stack
      can go as deep as m × n (a single long snake of cells). On balanced,
      sparse grids the depth is O(min(m, n)).
"""
