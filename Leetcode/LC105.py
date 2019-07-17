#solution1
# 由于preorder的特殊性，我们只需要依次pop(0) preorder，并且保证递归先进左子树，再进右子树就可以
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
         
        return self.build(preorder,inorder)
            
            
    def build(self,preorder,inorder):
        if not inorder:
            return None
        root = preorder.pop(0)
        i = 0
        while inorder[i] != root:
            i+=1
        left = inorder[:i]
        right = inorder[i+1:]
        
        rootNode = TreeNode(root)
        rootNode.left = self.build(preorder,left) 
        rootNode.right = self.build(preorder,right)
        return rootNode
		
# solution2
# 常规思路
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
         
        return self.build(preorder,inorder)
            
            
    def build(self,preorder,inorder):
        if not preorder or not inorder:
            return None
        root = preorder[0]
        i = 0
        while inorder[i] != root:
            i+=1
        left = inorder[:i]
        right = inorder[i+1:]
        right_length, left_length = len(right),len(left)
        
        rootNode = TreeNode(root)
        rootNode.left = self.build(preorder[1:1+left_length],left) 
        rootNode.right = self.build(preorder[1+left_length:],right)
        return rootNode