from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

       evenSum = sum(x for x in nums if x % 2 == 0)
       ans = []

       for val,idx in queries:

        if nums[idx] % 2 == 0: 
            evenSum -= nums[idx] # we know that if its even it was even number we will again add it
        nums[idx] += val #adding the query value
        if nums[idx] % 2 == 0: 
            evenSum += nums[idx]
        ans.append(evenSum)

       return ans


# driver code
nums = [1,2,3,4]

queries = [[1,0],[-3,1],[-4,0],[2,3]]

sol = Solution()
res = sol.sumEvenAfterQueries(nums, queries)
print("solution is ", res)
