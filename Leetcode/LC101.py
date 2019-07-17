class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.helper(root,root)
        
        
    def helper(self, p,q):
        if not q and p:
            return False
        if q and not p:
            return False
        if not q and not p:
            return True
        if q and p:
            if q.val == p.val:
                return self.helper(p.right,q.left) and self.helper(p.left,q.right)
            else:
                return False