
# https://leetcode.com/problems/path-sum-iii/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        result = 0

        def dfsTraverse(node,pathVal,targetSum):

            if node == None :
                return False
                  
        
            pathVal.append(node.val)     
            
            localSum = 0
            nonlocal result
            for i in range(len(pathVal) -1,-1,-1):
                localSum += pathVal[i]
                if localSum == targetSum:
                    result += 1

            dfsTraverse(node.left,pathVal,targetSum)
            dfsTraverse(node.right,pathVal,targetSum)

            pathVal.pop()

        
        dfsTraverse(root,[],targetSum)

        return result


        



# driver code
targetSum = 8
root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(-3)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)


sol = Solution()
res = sol.pathSum(root,targetSum)
print("solution is ", res)