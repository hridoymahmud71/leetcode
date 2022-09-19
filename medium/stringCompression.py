
# https://leetcode.com/problems/string-compression/
from itertools import count
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        prevChar = chars[0]
        counter = 1
        result = []

        for i in range(1,len(chars)):
            if chars[i] != prevChar:
                result.append(prevChar)
                if counter > 1:   
                    strCount =  str(counter)           
                    for capp in strCount:
                        result.append(capp)
                prevChar = chars[i]
                counter = 1
            else:
                counter += 1

        result.append(prevChar)
        if counter > 1:   
            strCount =  str(counter)           
            for capp in strCount:
                result.append(capp)
        

        chars[:] = result

        return len(chars)               



# driver code
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]


sol = Solution()
res = sol.compress(chars)
print("solution is ", res)