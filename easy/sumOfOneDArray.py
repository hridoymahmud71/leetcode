# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        
        for i in range(1,len(nums)):
            nums[i] = nums[i - 1] + nums[i]            

        return nums


# driver code
nums = [1,2,3,4]
sol = Solution()
res = sol.removeDuplicates(nums)
print("solution is ", res)