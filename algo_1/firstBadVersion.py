# https://leetcode.com/problems/first-bad-version/
import time

import random

class Solution:
    def firstBadVersion(self,n:int) -> int:

        #the isBadVersion method will be predefined in the api and defination will not be needed in leetcode submission
        def isBadVersion(x):
            return random.random() > .85

        low,high = 0,n
        

        while low < high:
            mid = low + (high - low) // 2
            if(isBadVersion(mid)):
                high = mid
            else : 
                low = mid + 1
        return low

# driver code 
sol = Solution()
start_time = time.time()
res = sol.firstBadVersion(17000000000000000000)
print(res,time.time()-start_time)