# https://leetcode.com/problems/max-area-of-island/

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        maxCounter = 0

        def traverseDFS(r, c):

            counter = 0
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1):
                return 0

            grid[r][c] = 0
            counter += 1

            counter += traverseDFS(r, c-1)  # left
            counter += traverseDFS(r, c+1)  # right
            counter += traverseDFS(r-1, c)  # top
            counter += traverseDFS(r+1, c)  # bottom

            return counter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxCounter = max(maxCounter, traverseDFS(r, c))
        return maxCounter


# driver code
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
sol = Solution()
res = sol.maxAreaOfIsland(grid)
print("solution is ", res)
