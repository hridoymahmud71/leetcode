#https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/submissions/
from typing import List

class Solution:
    def pivotIndex(self, arr: List[int]) -> bool:
        
        wholeSum = sum(arr)
        if wholeSum % 3 != 0 : 
            return False;
        
        targetSum = wholeSum / 3 # our goal is that each part should be 1/3 of the whole
        partCount = 0
        tempSum = 0

        for i,num in enumerate(arr):
            tempSum += num
            if(tempSum == targetSum):
                tempSum = 0;
                partCount += 1
            
            if partCount == 3:
                return True

        return False
    
        

#driver code
nums = [1,-1,1,-1]
sol = Solution()
res = sol.pivotIndex(nums)
print("solution is ",res)