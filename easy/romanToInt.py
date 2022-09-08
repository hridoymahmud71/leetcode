
# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0

        for i in range(len(s)):

            # if last character or current char val is greater than the next one
            if i == len(s) - 1 or mapping[s[i]] >= mapping[s[i+1]]:
                sum += mapping[s[i]]
            else:
                sum -= mapping[s[i]]

        return sum


# driver code
s = "III"
sol = Solution()
res = sol.romanToInt(s)
print("solution is ", res)
