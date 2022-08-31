# In order traversal https://leetcode.com/problems/binary-tree-inorder-traversal/
# Pre order traversal https://leetcode.com/problems/binary-tree-preorder-traversal/
# Post order traversal https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   
    def inOrderTraversal( root ):
        #print(root.toString())
        def doInOrderTraversal(root):
            if root:
                doInOrderTraversal(root.left)
                listOfInt.append(root.val)
                doInOrderTraversal(root.right)
            
        
        listOfInt = []
        doInOrderTraversal(root)
        return listOfInt

    def preOrderTraversal( root ):
        #print(root.toString())
        def doPreOrderTraversal(root):
            if root:
                listOfInt.append(root.val)
                doPreOrderTraversal(root.left)                
                doPreOrderTraversal(root.right)
            
        
        listOfInt = []
        doPreOrderTraversal(root)
        return listOfInt

    def postOrderTraversal( root ):
        #print(root.toString())
        def doPostOrderTraversal(root):
            if root:
                doPostOrderTraversal(root.left)                
                doPostOrderTraversal(root.right)
                listOfInt.append(root.val)
            
        
        listOfInt = []
        doPostOrderTraversal(root)
        return listOfInt
        
        
            
#image of tree here https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif          
# driver code

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol1 = Solution.inOrderTraversal(root);
sol2 = Solution.preOrderTraversal(root);
sol3 = Solution.postOrderTraversal(root);

print(sol1);
print(sol2);
print(sol3);