#https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        numSet = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        
        def str_to_int(num):
            
            value = 0
            multiplyBy = 1
            
            for i in range(len(num) -1,-1,-1): # decrease each index untill the array is emty
                value += numSet[num[i]] * multiplyBy
                multiplyBy *= 10
            
            return value
            
        return str_to_int(num1) + str_to_int(num2)
                
        
        

#driver code
num1 = "11"
num2 = "123"
sol = Solution()
res = sol.addStrings(num1,num2)
print("solution is ",res)