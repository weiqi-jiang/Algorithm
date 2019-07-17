# 用list 辅助
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depths = []
        self.helper(root,1,depths)
        return min(depths)
        
        
    def helper(self,root,depth,depths):
        if not root.left and not root.right:
            depths.append(depth)
            return 
        if root.left:
            self.helper(root.left,depth+1,depths)
        if root.right:
            self.helper(root.right,depth+1,depths)
			
# 不需要辅助
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depths = []
        return self.helper(root,1)
        
        
        
    def helper(self,root,depth):
        if not root:
            return None
        
        leftdepth = self.helper(root.left,depth+1)
        rightdepth  = self.helper(root.right,depth+1)
        
        if root.left and root.right:
            return min(leftdepth,rightdepth)
        if root.left and not root.right:
            return leftdepth
        if root.right and not root.left:
            return rightdepth
        return depth