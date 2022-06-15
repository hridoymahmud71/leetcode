# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1
        end = x
        ans = 0
       
        # divide and conqure   
        # while start < end :
        #     mid = start + (end - start) // 2
            
        #     print('start loop')
        #     print(start,end,"||",mid,mid*mid)
            
        #     if mid * mid == x :
        #         return mid
        #     elif mid * mid < x :
        #         start = mid + 1
        #         ans = start
        #     else :
        #         end = mid - 1
        #         ans = end
        #     print(ans)
        #     print('end loop\n')

        # brute force
        if x > 2:
            rangeEnd = x
            for i in(range(1,rangeEnd)):
                isquare = i * i
                if isquare == x:
                    ans = i
                    break
                if(isquare > x):
                    ans = i -1
                    break
        elif x == 1 or x == 2:
            ans = 1
        else :
            ans = 0 
            
                
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