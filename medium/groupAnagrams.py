# https://leetcode.com/problems/group-anagrams/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)

        final = []
        for value in h.values():
            final.append(value)
        return final


# driver code
strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
res = sol.groupAnagrams(strs)
print("solution is ", res)