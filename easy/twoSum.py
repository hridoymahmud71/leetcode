
# https://leetcode.com/problems/two-sum/


from typing import List

class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:

        keeping = {}
        for i in range(len(nums)):
            print(keeping)
            if nums[i] in keeping.keys():
                return [keeping[nums[i]],i]
            else:
                complement  = target - nums[i]
                keeping[complement]  = i


        
                    
        
                
        
        

#driver code
nums = [2,7,11,15]
target = 9
sol = Solution()
res = sol.twoSum(nums,target)
print("solution is ",res)