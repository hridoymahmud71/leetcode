

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        

        if root == None :
            return False        

        
        targetSum -= root.val

        if targetSum == 0 and root.left == None and root.right == None:
            return True

        print(root.val,targetSum)
        
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)

        



# driver code
targetSum = 22
root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)


sol = Solution()
res = sol.hasPathSum(root,targetSum)
print("solution is ", res)