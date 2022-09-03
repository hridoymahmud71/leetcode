# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1.0

        absn = abs(n)

        y = 1
        while absn > 1:
            if absn % 2 == 0:
                x = x * x
                absn = absn / 2
            else :
                y = x * y
                x = x * x
                absn = (absn - 1) / 2
            
        return x * y if n > 0 else 1 / (x * y)






# driver code
x = 2.00000
n = -2
sol = Solution()
res = sol.myPow(x,n)
print("solution is ", res)