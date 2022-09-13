#https://leetcode.com/problems/best-time-to-buy-and-sell-stock


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        globalMax = 0
        buyPrice = prices[0]

        for i in range(1,len(prices)):

            if prices[i] < buyPrice:
                buyPrice = prices[i]

        
            if (prices[i] - buyPrice) > globalMax :
                globalMax = prices[i] - buyPrice

        return globalMax

                
        
        

#driver code
prices = [7,6,4,3,1]
sol = Solution()
res = sol.maxProfit(prices)
print("solution is ",res)