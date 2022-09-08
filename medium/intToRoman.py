

# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        characters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];    

        ptr = 0 # this points to the index of values
        str = ""
        while(num > 0):
            reminder = num % values[ptr]

            # cound not divide
            if reminder == num :
                ptr += 1
            else:
                str += characters[ptr]
                num -= values[ptr] # as we are not shifting the pointer in this case , changing the value of num itself will make it follow the first case in the next iteration

        return str


# driver code
num = 147570
sol = Solution()
res = sol.intToRoman(num)
print("solution is ", res)
