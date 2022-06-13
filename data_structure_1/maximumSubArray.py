
# https://leetcode.com/problems/maximum-subarray/
# solving using divide and conquer

from typing import List

class Solution :
    def maxSubArray(self,nums:List[int]) -> int:
        n = len(nums) - 1 # final index

        return self.maxSubArraySum(nums,0,n)

    def maxSubArraySum(self,arr,low,high) -> int:
        #base case 
        if(low == high):
            return arr[low]
        

        mid = low + (high - low) // 2

        # 1. max subarray of left half
        # 2. max subarray of right half
        # 3. max subarray sum such that the subarray crosses the midpoint

        print(low,mid,high)
        max_sum = max(self.maxSubArraySum(arr,low,mid),self.maxSubArraySum(arr,mid + 1,high),self.maxCrossingSum(arr, low, mid, high))
        #return this largest possible sum of the section recursively
        return max_sum

    def maxCrossingSum(self,arr, low, mid, high) -> int:
        left_temp_sum = 0;
        right_temp_sum = 0;
        large_negative_number = -10000000000
        left_sum    = large_negative_number 
        right_sum   = large_negative_number

        #left part
        for i in range(mid,low-1,-1):
            left_temp_sum = left_temp_sum + arr[i]
            if(left_sum > left_temp_sum):
                left_sum = left_temp_sum
        
        #right part
        for i in range(mid+1,high + 1,):
            right_temp_sum = right_temp_sum + arr[i]
            if(right_sum > right_temp_sum):
                right_sum = right_temp_sum

        return max(left_sum,right_sum,left_sum + right_sum)

# driver code
arr = [2, 3, 4, 5, 10]
solution = Solution()
result = solution.maxSubArray(arr)
print(result)


