class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        low = -float('inf')
        high = float('inf')
        
        return self.helper(low,high,root)    
        
        
        
    def helper(self,low,high,root):
        if not root:
            return True
        
        if root.val<=low or root.val>=high:
            return False
        return self.helper(low,root.val,root.left) and self.helper(root.val,high,root.right)