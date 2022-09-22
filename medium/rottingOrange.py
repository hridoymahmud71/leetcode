# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        nr = len(grid)
        nc = len(grid[0])
        freshCount = 0
        rottenPositionQueue = deque()

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    freshCount += 1
                elif grid[r][c] == 2:
                    rottenPositionQueue.append((r, c))

        # We are taking a temp queue as
        # To count a minute we need the number of new rotten oranges on that cycle
        tempRottenPositionQueue = deque()
        while rottenPositionQueue:

            r, c = rottenPositionQueue.popleft()

            if r < nr - 1 and grid[r + 1][c] == 1:
                grid[r + 1][c] = 2
                tempRottenPositionQueue.append((r + 1, c))
            if r > 0 and grid[r - 1][c] == 1:
                grid[r - 1][c] = 2
                tempRottenPositionQueue.append((r - 1, c))
            if c < nc - 1 and grid[r][c + 1] == 1:
                grid[r][c + 1] = 2
                tempRottenPositionQueue.append((r, c + 1))
            if c > 0 and grid[r][c - 1] == 1:
                grid[r][c - 1] = 2
                tempRottenPositionQueue.append((r, c - 1))

            if len(rottenPositionQueue) == 0 and freshCount > 0:
                rottenPositionQueue += tempRottenPositionQueue  # deque merge
                freshCount -= len(tempRottenPositionQueue)
                tempRottenPositionQueue.clear()
                minutes += 1

        return minutes if freshCount == 0 else - 1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
sol = Solution()
res = sol.orangesRotting(grid)
print("solution is ", res)
