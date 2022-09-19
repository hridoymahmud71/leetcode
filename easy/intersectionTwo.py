
# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        bigger = nums1 if len(nums1) >= len(nums2) else nums2
        smaller = nums1 if len(nums1) < len(nums2) else nums2
            
        result = []
        dictWithBigger = {}

        for i in range(len(bigger)):
            if bigger[i] in  dictWithBigger.keys():
                 dictWithBigger[bigger[i]] +=1
            else:
                 dictWithBigger[bigger[i]] = 1


        for i in range(len(smaller)):
            
            if smaller[i] in dictWithBigger.keys() and dictWithBigger[smaller[i]] > 0:
                result.append(smaller[i])
                dictWithBigger[smaller[i]] -= 1
                
        return result

# driver code
nums1 = [1,2]
nums2 = [1,1]

sol = Solution()
res = sol.intersection(nums1,nums2)
print("solution is ", res)