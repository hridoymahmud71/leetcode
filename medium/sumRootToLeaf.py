
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
               
        sum = 0

        def dfsTraverse(node,pathVal):
            nonlocal sum

            if node == None :
                return False
                  
            # print(node.val)
            pathVal.append(node.val)     
            

            if node.left == None and node.right == None:
                number = ''.join(map(str,pathVal))
                sum += int(number)

            # print(node.val,pathVal)    
            dfsTraverse(node.left,pathVal)
            dfsTraverse(node.right,pathVal)

            
            pathVal.pop()

        
        dfsTraverse(root,[])

        return sum


        



# driver code

root = TreeNode(4)

root.left = TreeNode(9)
root.right = TreeNode(0)

root.left.left = TreeNode(5)
root.left.right = TreeNode(1)


sol = Solution()
res = sol.sumNumbers(root)
print("solution is ", res)