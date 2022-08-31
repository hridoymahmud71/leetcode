
#https://leetcode.com/problems/find-pivot-index/ 
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        wholeSum = sum(nums)
        leftSum = 0
        
        for i,num in enumerate(nums):
            rightSum = wholeSum - num - leftSum
            print("righSum = ",wholeSum ,"-",num ,"-" ,leftSum)
            print("i:",i,",leftSum:",leftSum,",rightSum:",rightSum)
            if(leftSum == rightSum):
                return i
            else : leftSum += num
        return -1
    
        

#driver code
nums = [1,7,3,6,5,6]
sol = Solution()
res = sol.pivotIndex(nums)
print("solution is ",res)