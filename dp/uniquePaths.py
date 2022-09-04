# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:

        # -----start-----
        # recursive way Time Limit Exceeded
        # to move into a goal at each level we need to find out the unique path to it's previous two boxes unique path's sum
        # base cases
        # if m == 0 or n == 0:
        #     return 0

        # if m == 1 or n == 1:
        #     return 1

        # return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        # -----end-----


        # -----start-----
        # recursive way with memo  
        # memkey = str(m)+"-"+str(n)

        # if memkey in memo.keys():
        #     return memo[memkey]       


        # if m == 0 or n == 0:
        #     return 0

        # if m == 1 or n == 1:
        #     return 1

        # memo[memkey] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)

        # return memo[memkey]
        # -----end-----

        # another solution below
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]


# driver code
m = 23
n = 12
sol = Solution()
res = sol.uniquePaths(m, n)
print("solution is ", res)
