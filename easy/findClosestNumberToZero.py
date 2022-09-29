# https://leetcode.com/problems/find-closest-number-to-zero/submissions/
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        mymin = abs(nums[0])
        targetIndex = 0
        
        
        for i in range(1,len(nums)):
           
            if abs(nums[i]) <= mymin and nums[i] > nums[targetIndex]:
                mymin = abs(nums[i])
                targetIndex = i
                
                
            
        return nums[targetIndex]

# driver code
nums = [-4,-2,1,4,8]
sol = Solution()
res = sol.findClosestNumber(nums)
print("solution is ", res)