
# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        lptr = rptr = 0

        while rptr < len(nums):
            if nums[rptr] != 0:
                nums[lptr],nums[rptr] = nums[rptr],nums[lptr]
                lptr += 1 # only shift the left pointer if switchint happens
            rptr += 1 #always move the right pointer

        
        print(nums)


nums = [0, 1, 0, 3, 12]

k = 3
sol = Solution()
res = sol.moveZeroes(nums)
print("solution is ", res)
