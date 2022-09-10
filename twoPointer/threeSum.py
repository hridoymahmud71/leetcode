
# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []
        

        for i in range(len(nums)):

            lptr = i + 1
            rptr = len(nums) - 1

            # case [-1, -1, -1 ,..........]
            # lets say there are some continuous same numbers
            # then it will create duplicate result
            # although we are incrementing left pointer we are getting the same previous value and the outer while will execute the same way
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while (lptr < rptr):

                sum = nums[i] + nums[lptr] + nums[rptr]

                if sum == 0:
                    output.append([nums[i], nums[lptr], nums[rptr]])
                    lptr += 1
                    
                    # case [-1, -1, -1 ,..........]
                    # lets say there are some continuous same numbers
                    # then it will create duplicate result
                    # although we are incrementing left pointer we are getting the same previous value and the outer while will execute the same way
                    while (nums[lptr] == nums[lptr - 1] and lptr < rptr):
                        lptr += 1
                elif sum > 0:
                    rptr -= 1
                else:
                    lptr += 1

        return output


# driver code
nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
sol = Solution()
res = sol.threeSum(nums)
print("solution is ", res)
