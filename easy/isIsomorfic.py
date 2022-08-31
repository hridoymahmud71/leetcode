# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stMap, tsMap = {}, {}

        for i in range(len(s)):

            # 012   
            # foo
            # bar
            # on oth and 1th iteration the stMap = {f:b,o:a} tsMap = {b:f,a:o}

            # s[2] here is 'o' and it's already pushed in stMap but stMap[s[2]] / stMap[o] is r 'o->r'
            # t[2] here is 'r' and it's not pushed in tsMap but tsMap[t[2]] / tsMap[r] is o 'r->o'
            # if it's reversely mapping is should already be in the existing map but it's not. So it's a false case


            # 012   
            # foo
            # foo
           # on oth and 1th iteration the stMap = {f:f,o:ao} tsMap = {f:f,o:o}

            # s[2] here is 'o' and it's already pushed in stMap but stMap[s[2]] / stMap[o] is r 'o->o' which skips this case
            # t[2] here is 'o' and it's already pushed in tsMap but tsMap[t[2]] / tsMap[r] is o 'o->o' which skips this case
            # if it's reversely mapping is should already be in the existing map but it's not. So it's a true case

            if s[i] in stMap and stMap[s[i]] != t[i]:
                return False

            if t[i] in tsMap and tsMap[t[i]] != s[i]:
                return False

            # setting up the map
            stMap[s[i]] = t[i]
            tsMap[t[i]] = s[i]

        return True

# driver code
s = "foo"
t = "foo"
sol = Solution()
res = sol.isIsomorphic(s, t)
print("solution is ", res, type(res))
