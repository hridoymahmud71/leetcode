

# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(num:int)->bool:
        l,r = 0,num

        while l<=r:
            m = l + (r-l) // 2
            print("begin",m,l,r)
            if m**2 == num:
                return True
            elif m**2 < num:
                l = m + 1;
            else:
                r = m - 1;
            print("end",m,l,r)
        return False

num = 16
sol = Solution.isPerfectSquare(num)
print(sol)
