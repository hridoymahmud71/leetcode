# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)

        def reverseArray(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverseArray(nums, 0, len(nums) - 1)    
        reverseArray(nums, 0, k - 1)
        reverseArray(nums, k, len(nums) - 1)

        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]

k = 3
sol = Solution()
res = sol.rotate(nums, k)
print("solution is ", res)
