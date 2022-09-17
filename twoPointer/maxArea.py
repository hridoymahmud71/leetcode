

from typing import List
import time

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left],height[right])

            maxArea = max(maxArea,area)

            if height[left] < height[right]:
                left += 1
            else : 
                right -= 1

        return maxArea



# driver code

# get the start time
st = time.process_time()

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()



res = sol.maxArea(height)
print("solution is ", res)

# get the end time
et = time.process_time()

# get the execution time
elapsed_time = (et - st) * 1000


print('Execution time:', elapsed_time, 'ms')