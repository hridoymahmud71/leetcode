# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i][j] + triangle[i+1]
                                     [j], triangle[i][j] + triangle[i+1][j+1])
        return triangle[0][0]


# driver code
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
sol = Solution()
res = sol.minimumTotal(triangle)
print("solution is ", res)
