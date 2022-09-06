# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        numOfIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        def traverseDFS(r, c):

            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1"):
                return
                      

            grid[r][c] = "0"

            traverseDFS(r, c-1)  # left
            traverseDFS(r, c+1)  # right
            traverseDFS(r-1, c)  # top
            traverseDFS(r+1, c)  # bottom

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    traverseDFS(r, c)
                    numOfIslands += 1

        return numOfIslands


# driver code
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
sol = Solution()
res = sol.numIslands(grid)
print("solution is ", res)
