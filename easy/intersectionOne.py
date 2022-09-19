
# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        bigger = nums1 if len(nums1) >= len(nums2) else nums2
        smaller = nums1 if len(nums1) < len(nums2) else nums2
            
        result = []
        for i in range(len(smaller)):
            if smaller[i] in bigger and smaller[i] not in result:
                result.append(smaller[i])
                
        return result

# driver code
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

sol = Solution()
res = sol.intersection(nums1,nums2)
print("solution is ", res)