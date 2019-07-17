class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        所有叶子节点的深度最大最小值相差不能大于1
        '''
        if not root:
            return True
        
        return self.helper(1,root) != -1
        
        
        
    def helper(self,depth,root):
        if not root:
            return depth
        
        leftdepth = self.helper(depth+1,root.left)
        rightdepth = self.helper(depth+1,root.right)
        if leftdepth == -1 or rightdepth == -1 or abs(leftdepth - rightdepth)>1:
		# 用-1来表示子树并不满足条件
            return -1
        # 这个max()要特别注意，对于每一个当前节点，返回它左右子树较深的那个的深度
        return max(leftdepth,rightdepth)