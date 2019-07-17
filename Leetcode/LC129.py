class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        res = []
        self.helper(0,root,res)
        return sum(res)
        
        
        
    def helper(self,cur,root,res):
        
        cur  = cur*10 + root.val
        if not root.left and not root.right:
            res.append(cur)
        else:
            if root.left:
                self.helper(cur,root.left,res)
            if root.right:
                self.helper(cur,root.right,res)