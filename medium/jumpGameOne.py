
# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # greedy approach https://youtu.be/Yan0cv2cLy8?t=616

        goalPost = len(nums) - 1

        for i in range(len(nums) - 1, -1 , -1): # decrement by one from last to beginning
            
            # [2, 3, 1, 1, 4] indices 0,1,2,3,4

            # i == 4 , 4 + 4 >  4 , so goalPost is shifted to 4
            # i == 3 , 3 + 1 =  4 , so goalPost is shifted to 3
            # i == 2 , 2 + 1 =  3 , so goalPost is shifted to 2
            # i == 1 , 1 + 3 >  3 , so goalPost is shifted to 1
            # i == 0 , 0 + 2 >  1 , so goalPost is shifted to 0
            
            if i + nums[i] >= goalPost:
                goalPost = i

        return goalPost == 0 # if goalPost shifted to the beginning


# driver code
nums = [2, 3, 1, 1, 4]
sol = Solution()
res = sol.canJump(nums)
print("solution is ", res)
