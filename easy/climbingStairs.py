

#https://leetcode.com/problems/climbing-stairs/submissions/
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: 
            return n
    
        ways = [0 for _ in range(n)]
        ways[0] = 1
        ways[1] = 2
        
        for i in range(2, n):
            ways[i] += ways[i - 1] + ways[i - 2]
        
        return ways[n-1]
        

#driver code
n = 18
sol = Solution()
res = sol.climbStairs(n)
print("solution is ",res)