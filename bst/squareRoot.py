# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1
        end = x
        ans = 0
       
        while start < end :
            mid = start + (end - start) // 2
            
            print('start loop')
            print(start,end,"||",mid,mid*mid)
            
            if mid * mid == x :
                return mid
            elif mid * mid < x :
                start = mid + 1
                ans = start
            else :
                end = mid - 1
                ans = end
            print(ans)
            print('end loop\n')
                
        return ans

# driver code
while True:
    i = input("enter an integer (enter non integer to exit)")
    if i.isnumeric() == False:
        break
    i = int(i)
    if isinstance(i, int) == False:
        break

    sol =  Solution()
    res = sol.mySqrt(i)
    print('ans is: ',res)      

print("program ends")