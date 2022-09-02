
# https://leetcode.com/problems/jump-game-ii/

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:

        # https://www.youtube.com/watch?v=dJ7sWiOoK7g
        # Greedy approach with boundaries
        result = 0
        l = r = 0

        while r < len(nums) - 1:
            
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # shift the boundary
            l = r + 1
            r = farthest
            result += 1
        
        return result


# driver code
nums = [2,3,1,1,4]
sol = Solution()
res = sol.jump(nums)
print("solution is ", res)
