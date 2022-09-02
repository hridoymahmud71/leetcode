
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(len(words) - 1):
            # is not anagram then push
            if ''.join(sorted(words[i])) != ''.join(sorted(words[i+1])): 
                result.append(words[i+1])

        return result


# driver code
words = ["abba", "baba", "bbaa", "cd", "cd"]
sol = Solution()
res = sol.removeAnagrams(words)
print("solution is ", res)
