
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0


        def dfsTrasverse(current,level):
            if current == None :
                return level
            level += 1
            
            return max(dfsTrasverse(current.left,level),dfsTrasverse(current.right,level)) 
            

        
        return dfsTrasverse(root,0)

        



# driver code
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
res = sol.maxDepth(root)
print("solution is ", res)