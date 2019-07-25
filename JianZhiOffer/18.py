class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.helper(pRoot1, pRoot2)
    
    def helper(self,root1,root2):
        if root1.val == root2.val:
            if self.isSameStructure(root1,root2):
                return True
        
        if root1.left:
            return self.helper(root1.left,root2)
        if root1.right:
            return self.helper(root1.right,root2)
        return False
    
    def isSameStructure(self,root1,root2):
        if not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and root2:
            if root2.val == root1.val:
                return self.isSameStructure(root1.left,root2.left) and self.isSameStructure(root1.right,root2.right)
            else:
                return False