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

from collections import deque
from typing import List


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        DFS "sink the island" approach (mutates the input grid in place).
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

    def numIslandsBFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        BFS "sink the island" approach (mutates the input grid in place).
        Same idea as the DFS variant, but expands the island with a queue
        instead of the recursion stack.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        # Four cardinal directions.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # New island found — sink every cell of this component.
                    count += 1
                    queue = deque([(i, j)])
                    grid[i][j] = '0'
                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'      # mark visited in place
                                queue.append((nr, nc))

        return count


"""
Solution (two equivalent flood-fill variants):
1. Scan the grid cell by cell. Each time an unvisited land cell ('1') is found,
   increment the island counter and launch a traversal (DFS or BFS) to flood-
   fill the entire connected landmass.
2. The traversal visits a cell, marks it as water ('0') in place to record the
   visit — the "sink the island" trick — so no separate visited data structure
   is needed, then expands to the four cardinal neighbors.
3. After the traversal completes, the whole connected component is marked, so
   it is never counted again.

- DFS version (numIslands): recursive calls, depth-first. Recursion stack
  holds the active path.
- BFS version (numIslandsBFS): explicit queue, breadth-first. Queue holds the
  current frontier.

Time:  O(m × n) — every cell is visited at most once in both variants.
Space: O(m × n) worst case —
       * DFS: recursion stack can reach depth m×n on an all-land grid.
       * BFS: the queue can hold ~half the cells (m×n/2) on an all-land grid.
       Average on sparse grids: O(min(m, n)) for DFS, O(min(m, n)) for BFS.

Note: both versions mutate the input grid in place. If mutating is not
allowed, trade the sink step for a separate visited set (adds O(m×n) space).
"""
