class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        
        return self.build(inorder,postorder)
        
        
    def build(self,inorder,postorder):
        '''
        postorder: left,right,root
        inorder: left root right
        '''
        if not inorder:
            return None
        rootvalue = postorder.pop()
        root = TreeNode(rootvalue)
        index = inorder.index(rootvalue)
        root.right = self.build(inorder[index+1:],postorder)
        root.left = self.build(inorder[:index],postorder)
        return root