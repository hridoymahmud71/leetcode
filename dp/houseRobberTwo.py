
# https://leetcode.com/problems/house-robber-ii/
from re import A
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:    

        if len(nums) == 1:
            return nums[0]

        numsX = nums[1:] # removing first item
        numsY = nums[:-1] # removing last item
        
        print(nums,numsX,numsY)

        if len(numsX) == 1 or len(numsY) == 1  :
            return max(numsX[0],numsY[0])
        
    
        dpX = {}
        dpX[0] = numsX[0]
        dpX[1] = max(numsX[0],numsX[1])

        dpY = {}
        dpY[0] = numsY[0]
        dpY[1] = max(numsY[0],numsY[1])

        


        for i in range(2,len(numsX)):
            dpX[i] = max(dpX[i-2] + numsX[i] , dpX[i-1])

        for i in range(2,len(numsX)):
            dpY[i] = max(dpY[i-2] + numsY[i] , dpY[i-1])

        return max(dpX[len(numsX) - 1],dpY[len(numsY) - 1])


# driver code
nums = [2,3]
sol = Solution()
res = sol.rob(nums)
print("solution is ", res)