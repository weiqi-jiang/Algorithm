class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.helper(0,root,sum)
        
        
    def helper(self,add,root,sum):
        if not root:
            return False
        add+= root.val
        if not root.left and not root.right:
            if add == sum:
                return True
            return False
        
        return self.helper(add,root.left,sum) or self.helper(add,root.right,sum)