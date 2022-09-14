

# https://leetcode.com/problems/move-zeroes/

from typing import List


# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while (l < r):
            mysum =  numbers[l] + numbers[r]
            if mysum == target:
                return [l+1,r+1]
            elif mysum < target:
                l +=1
            else:
                r -=1

        # for i in range(len(numbers)):
        #     l, r = i + 1, len(numbers)-1
        #     complement = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if numbers[mid] == complement:
        #             return [i+1, mid+1]
        #         elif numbers[mid] < complement:
        #             l = mid+1
        #         else:
        #             r = mid-1


numbers = [2, 7, 11, 15]
target = 9

sol = Solution()
res = sol.twoSum(numbers, target)
print("solution is ", res)
