
# https://leetcode.com/problems/path-sum-ii/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []

        def dfsTraverse(node,pathVal,targetSum):

            if node == None :
                return False
                  
        
            pathVal.append(node.val)     
            targetSum -= node.val

            if targetSum == 0 and node.left == None and node.right == None:
                result.append(pathVal.copy())

            dfsTraverse(node.left,pathVal,targetSum)
            dfsTraverse(node.right,pathVal,targetSum)

            pathVal.pop()

        
        dfsTraverse(root,[],targetSum)

        return result


        



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
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)


sol = Solution()
res = sol.pathSum(root,targetSum)
print("solution is ", res)