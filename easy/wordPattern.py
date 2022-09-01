
# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words, words_to_pattern = s.split(" "), {}

        if len(pattern) != len(words):
            return False

        # for the case w = ['dog', 'cat'] and p = 'aa'
        if len(set(pattern)) != len(set(words)): 
            return False 

        for i in range(len(words)):
            if words[i] not in words_to_pattern:
                words_to_pattern[words[i]] = pattern[i]
            elif words_to_pattern[words[i]] != pattern[i]: 
                return False        

        return True

        

# driver code
pattern = "aba"
s = "dog cat cat"
sol = Solution()
res = sol.wordPattern(pattern, s)
print("solution is ", res, type(res))    