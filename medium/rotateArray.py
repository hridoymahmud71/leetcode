# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        part1 = nums[0: k+1]
        part2 = nums[k+1: len(nums)]

        numsNew = part2 + part1

        for i in range(len(numsNew)):
            nums[i] = numsNew[i]

        print(nums)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
res = sol.rotate(nums, k)
print("solution is ", res)
