
#https://leetcode.com/problems/binary-tree-level-order-traversal
# write driver code yourself
from typing import List, Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        output  = {}
        def traverse(current,level):
            if current == None :
                return

            if level in output.keys():
                output[level].append(current.val)

            else :
                output[level] = [current.val]

            level += 1

            traverse(current.left,level)
            traverse(current.right,level)
            


        traverse(root,0)
        
        result  = []
        
        for i in output:
            result.append(output[i])
            

        return result

        