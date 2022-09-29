# https://leetcode.com/problems/find-k-closest-elements/

from math import inf
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        low = 0
        high = len(arr) - 1

        while (high - low >= k):

            lowDiff = abs(arr[low] - x)
            highDiff = abs(arr[high] - x)

            if lowDiff <= highDiff:
                high -= 1
            else:
                low += 1

        print(low,high)
        output = arr[low:high + 1]

        return output


# driver code
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
sol = Solution()
res = sol.findClosestElements(arr, k, x)
print("solution is ", res)
