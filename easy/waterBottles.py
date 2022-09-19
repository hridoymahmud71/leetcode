# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        result = numBottles # as we can drink at least the give nnumber of bottles
        while numBottles >= numExchange:

            exchangable = numBottles // numExchange
            reminder = numBottles % numExchange
            numBottles = exchangable + reminder # exchangable for next iteration
            result += exchangable

        return result


# driver code
numBottles = 9
numExchange = 3
sol = Solution()
res = sol.numWaterBottles(numBottles, numExchange)
print("solution is ", res, type(res))  