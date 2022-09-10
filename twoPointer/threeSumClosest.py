
# https://leetcode.com/problems/3sum-closest/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        globalClosestSum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):

            lptr = i + 1
            rptr = len(nums) - 1

            while (lptr < rptr):

                localSum = nums[i] + nums[lptr] + nums[rptr]

                if localSum == target:
                    return target
                
                # if the gap between localsum and target is lesser than the gap between globalsum and target then ,
                # localsum will become new globalsum
                if abs(localSum - target) < abs(globalClosestSum - target):

                    globalClosestSum = localSum

                # separate
                if localSum < target:
                    lptr += 1
                else:
                    rptr -= 1

        return globalClosestSum


# driver code
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
sol = Solution()
res = sol.threeSumClosest(nums, target)
print("solution is ", res)
