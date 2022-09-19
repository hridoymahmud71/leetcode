
# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
    

        nums1, nums2 = set(nums1), set(nums2)
        diff12 = list(nums1.difference(nums2))
        diff21 = list (nums2.difference(nums1))

        return [diff12,diff21]

        

# driver code
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

sol = Solution()
res = sol.findDifference(nums1,nums2)
print("solution is ", res)