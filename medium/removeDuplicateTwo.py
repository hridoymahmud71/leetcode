# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        prev = nums[0]
        total = 1
        i = 1 # 1 item is already taken as prev
        while(i < len(nums)):
             
            if nums[i] == prev:
                total += 1

                if total > 2:
                    del nums[i]
                    i -= 1
                    total -= 1

            else :
                total = 1
            
            prev = nums[i]
            i += 1

        return len(nums)

# driver code
nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
res = sol.removeDuplicates(nums)
print("solution is ", res)

