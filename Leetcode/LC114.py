class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        root,_ = self.helper(root)
       
        
        
    def helper(self,root):
        
        if not root.left and not root.right:
            return root,root
        if root.left and root.right:
            leftfirst,leftlast = self.helper(root.left)
            rightfirst,rightlast  =self.helper(root.right)
            root.right = leftfirst
            root.left = None
            leftlast.right = rightfirst
            return root,rightlast
        if root.left and not root.right:
            leftfirst,leftlast = self.helper(root.left)
            root.right = leftfirst
            root.left = None
            return root,leftlast
        if root.right and not root.left:
            rightfirst,rightlast  =self.helper(root.right)
            return root,rightlast