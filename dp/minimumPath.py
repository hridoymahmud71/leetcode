# https://leetcode.com/problems/unique-paths/

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]], memo=[]) -> int:

        m = len(grid) 
        n = len(grid[0])

        hit = 0

        # -----start-----
        # recursive way with memo

        
        # memo = {}

        # def dfsTraverse(m, n, memo):
            

        #     memkey = str(m)+"-"+str(n)

        #     if memkey in memo.keys():
        #         return memo[memkey]

            

        #     if m == 0 and n == 0:
        #         return grid[m][n]

        #     if m < 0 or n < 0:
        #         return float('inf')

        #     memo[memkey] = min(dfsTraverse(m-1, n, memo),
        #                        dfsTraverse(m, n-1, memo)) + grid[m][n]
        #     return memo[memkey]

        # return  dfsTraverse(m-1, n-1, memo)

        # -----end-----

        # another solution below
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                elif r > 0 and c > 0:
                    dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + grid[r][c]
                elif r > 0 and c == 0:
                    dp[r][c] = dp[r-1][c] + grid[r][c]
                elif r == 0 and c > 0:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
        return dp[m-1][n-1]


# driver code
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
sol = Solution()
res = sol.minPathSum(grid)
print("solution is ", res)
