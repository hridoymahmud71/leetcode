# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:

        keeper = set()
        counter = 0

        for i in range(len(s)):
            if s[i] in keeper:
                counter += 2 # if it existed that means with current item it creates a pair of the item
                keeper.remove(s[i]) #  remove a paired item

            else:
                keeper.add(s[i])

        
        return counter if len(keeper) == 0 else counter + 1

                


    

# driver code
s = "abccccdd"
sol = Solution()
res = sol.longestPalindrome(s)
print("solution is ", res)