
# https://leetcode.com/problems/01-matrix/

import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        numRows = len(mat)
        numcols = len(mat[0])

        dp  = [[math.inf for x in range(numcols)] for y in range(numRows)] # fill 2d array with infinity

        for r in range(numRows):
            for c in range(numcols):
                if mat[r][c] == 0:
                    dp[r][c] = 0
                else:
                    if r > 0 :
                        dp[r][c] = min(dp[r][c],dp[r - 1][c] + 1)
                    if c > 0 :
                        dp[r][c] = min(dp[r][c],dp[r][c - 1] + 1)

        for r in range(numRows - 1,-1,-1):
            for c in range(numcols - 1,-1,-1):
            
                if r < numRows - 1 :
                    dp[r][c] = min(dp[r][c],dp[r + 1][c] + 1)
                if c < numcols - 1 :
                    dp[r][c] = min(dp[r][c],dp[r][c + 1] + 1)


        return dp

        # visited = set()
        # from collections import deque
        # q = deque()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             visited.add((i,j))
        #             q.append((i,j))
        
        # while q:
        #     x,y = q.popleft()
        #     for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
        #         newX, newY = x+dirr[0], y+dirr[1]
        #         if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
        #                 matrix[newX][newY] = matrix[x][y] + 1
        #                 visited.add((newX, newY))
        #                 q.append((newX, newY))
        # return matrix

# driver code
mat = [[0],[0],[0],[0],[0]]
sol = Solution()
res = sol.updateMatrix(mat)
print("solution is ", res)

        