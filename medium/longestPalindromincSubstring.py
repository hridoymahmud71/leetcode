
# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:

        localMaxSub = ""
        globalMaxSub = ""
        reversedS =  s[::-1]

        if(len(s) == 1) :
            return s

        for i in range (len(s)):
            if s[i] == reversedS[i]:
                localMaxSub += ""
            else :
                localMaxSub = s[i]
            
            if(len(localMaxSub) > len(globalMaxSub)):
                globalMaxSub = localMaxSub
            
        return globalMaxSub



        return ""

# driver code
s = "babad"
sol = Solution()
res = sol.longestPalindrome(s)
print("solution is ", res)