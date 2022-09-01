
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from threading import local


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Mehedi solution starts, Runtime: 5459 ms horrible solution
        # maxLength = 0
        # localMax = 0
        # subStr = []

        # i = 0
        # while (i < len(s)):
        #     currentChar = s[i]
        #     if s[i] in subStr:     

        #         # for dvdf in i = 2 we find d again, so we need to move back to the point after the previous d which was v  
        #         # that means i = 2 - {{ localMax - 1  = 2 - 1 for [dv] }} 
        #         i = i - (localMax - 1 )         
        #         subStr.clear()
        #         localMax = 0
        #     else :
        #         subStr.append(s[i])
        #         localMax += 1
        #         i += 1

        #     if localMax > maxLength:
        #         maxLength = localMax
           
        # return maxLength
        # Mehedi solution ends

        # Better solution starts runtime ~80 ms  https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1979/Simple-Javascript-Code
        maxLength = 0
        localMax = 0
        map = {}

        for i in range(len(s)):
            currentChar = s[i]
            
            # check to see if character has been encountered before. if so, and the index was equal to or greater than the current localMax, reset localMax to index it was seen plus 1. 
            # important because if the index it was last seen is less than localMax that means localMax isn't incremented up, making it easier to use it to update our maxLengthbelow
            # if it was encountered at a high index that means it will be harder to increase our maxLengthsince there is a repeat character pretty close to the current character
            # new characters don't result in localMax being increased since the lookup returns undefined which will return false for the evaluation
            # this makes it easy for maxLengthto be increased since that calculation looks at the index we are currently at which will always be pretty high since the loop always moves right

            if currentChar in map and map[currentChar] >= localMax:
                localMax  = map[currentChar] + 1        

            #  always update the index number we saw a character in the map 
            map[currentChar] = i

            #  use localMax to determine to update maxLength or not. adding 1 here offsets the addition of 1 when localMax is recalculated
            #  its used to determine if adding the current character is to our advantage or not as localMax holds a reference to how far away our last repeat is
            #  subtracting current index from how far away last repeat gives us that difference and the 1 says to update or not. note it has to be greater for it to be worth updating
            if  maxLength < (i - (localMax - 1)):
                maxLength = i - (localMax - 1)
   
        return maxLength
        # Better solution ends

        
        
s = "dvdf"
sol = Solution()
res = sol.lengthOfLongestSubstring(s)
print("solution is ", res)  