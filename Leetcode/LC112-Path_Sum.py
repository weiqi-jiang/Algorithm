"""
第一反应是遍历找到每一条root_to_leaf的sum 然后判断是否存在相等
但其实没必要，是否存在就是(左子树是否存在sum-root.val) or (右子树是否存在sum-root.val)
"""
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