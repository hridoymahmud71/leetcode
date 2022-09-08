# https://leetcode.com/problems/powx-n/

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        # -------------Hridoy solution starts------------
        # if len(nums) == 0:
        #     return nums[0]

        # globalSums = nums

        # for outer in range(len(nums) - 1):
        #     localSum = []

        #     for inner in range(len(globalSums) - 1):
        #         addable = globalSums[inner] + globalSums[inner + 1]
        #         last_digit = int(repr(addable)[-1]) # last digit

        #         localSum.append(last_digit)
        #     globalSums = localSum

        # return globalSums[0]
        # -------------Hridoy solution ends------------



        # -------------Mehedi solution starts------------        
        while (len(nums) > 1):

            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            
            nums.pop()

        return nums[0]
        # -------------Hridoy solution ends--------------


# driver code
nums = [1, 2, 3, 4, 5]
sol = Solution()
res = sol.triangularSum(nums)
print("solution is ", res)
