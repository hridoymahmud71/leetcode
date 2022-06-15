# https://leetcode.com/problems/sqrtx/

import math 


class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1
        end = x
        ans = 0
       
        # divide and conqure   
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
        # divide and conqure ends

        
        # brute force
        # if x > 2:          
        #     for i in(range(1,x)):
        #         isquare = i * i
        #         if isquare == x:
        #             ans = i
        #             break
        #         if(isquare > x):
        #             ans = i -1
        #             break
        # elif x == 1 or x == 2:
        #     ans = 1
        # else :
        #     ans = 0 
        #brute force ends 
            
                
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
    actual_result = int(math.sqrt(i))
    print('ans is: ',res, ' the actual result is ',actual_result ,'Answer is ',res == actual_result)      

print("program ends")