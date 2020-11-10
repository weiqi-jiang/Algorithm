"""
递归判断 recursive approach
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        return self.helper(p,q)
        
        
    def helper(self,p,q):
        if p and not q:
            return False
        if q and not p:
            return False
        if not q and not p:
            return True
        if q and p:
            if p.val == q.val:
                return self.helper(p.left,q.left) and self.helper(p.right,q.right)
            else:
                return False