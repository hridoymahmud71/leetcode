
from typing import List

class Solution:
    def peakIndexInMountainArray(arr: List[int]) -> int:
        l , r =  0 , len(arr) - 1
        
        if r < 2:
            return -1
        
        while l < r :
            m =  (l + r) // 2
            
            if arr[m] < arr[m + 1] :
                l = m + 1
            else:
                r = m
        return l

arr =  [3,4,5,1]
sol = Solution.peakIndexInMountainArray(arr);

print(sol);