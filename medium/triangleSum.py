# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        pos = 0    
        sum = 0
        for i in range(len(triangle)):

            if i == 0:
                sum += triangle[i][pos]

            else:
                if triangle[i][pos] < triangle[i][pos + 1]:
                    sum += triangle[i][pos]                
                else:
                    sum += triangle[i][pos + 1]
                    pos += 1
            
            print(sum,pos)
    
        return sum
       





       

# driver code
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
sol = Solution()
res = sol.minimumTotal(triangle)
print("solution is ", res)