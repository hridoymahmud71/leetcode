
# https://leetcode.com/problems/house-robber/
from re import A
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        # ----------- without dp starts -----------
        # prev = 0
        # curr = 0

        # for i in range(len(nums)):

        #     temp = max(prev + nums[i], curr)
        #     prev = curr
        #     curr = temp

        # return curr
        # ----------- without dp ends -----------

        # with dp

        #base cases 
        if len(nums) == 1:
            return nums[0]

        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])


        for i in range(2,len(nums)):

            dp[i] = max(dp[i-2] + nums[i] , dp[i-1])

        return dp[len(nums) - 1]


# driver code
nums = [2, 1, 1, 2]
sol = Solution()
res = sol.rob(nums)
print("solution is ", res)
