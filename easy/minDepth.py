
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        mindepth = 0
        myqueue = deque()
        myqueue.append(root)
        
        while myqueue :
            currentLevelSize = len(myqueue) 
            mindepth += 1

            for i in range(currentLevelSize):
                current =  myqueue.popleft()

                if current.left == None and current.right == None :
                    return mindepth
                
                if current.left:
                    myqueue.append(current.left)
                if current.right:
                    myqueue.append(current.right)
        
        return mindepth


# driver code
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
res = sol.minDepth(root)
print("solution is ", res)
