# https://leetcode.com/problems/group-anagrams/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Hridoy solution starts 115 ms
        # mapS = {}
        # mapT = {}

        # for i in range(len(s)):

        #     if s[i] in mapS.keys():
        #         mapS[s[i]] += 1
        #     else:
        #         mapS[s[i]] = 1

        # for i in range(len(t)):

        #     if t[i] in mapT.keys():
        #         mapT[t[i]] += 1
        #     else:
        #         mapT[t[i]] = 1

        # return mapS == mapT
        # Hridoy solution ends

        # Mehedi solution starts  85 ms
        # mapS = {}

        # for i in range(len(s)):

        #     if s[i] in mapS.keys():
        #         mapS[s[i]] += 1
        #     else:
        #         mapS[s[i]] = 1

        # for i in range(len(t)):

        #     if t[i] in mapS.keys():
        #         mapS[t[i]] -= 1
        #         if mapS[t[i]] == 0:
        #             del mapS[t[i]]
                
        #     else:
        #         return False
        # # print(mapS)
        # return len(mapS) == 0
        # Mehedi solution ends

        # easy  Solution 110 ms
        return ''.join(sorted(s)) == ''.join(sorted(t))


# driver code
s = "a"
t = "a"
sol = Solution()
res = sol.isAnagram(s, t)
print("solution is ", res)
