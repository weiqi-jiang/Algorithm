class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        maxdepth = [0]
        self.helper(root,1,maxdepth)
        return maxdepth[-1]
        
    def helper(self,root,depth,maxdepth):
        maxdepth[-1] = max(maxdepth[-1],depth)
        if root.left:
            self.helper(root.left,depth+1,maxdepth)
        if root.right:
            self.helper(root.right,depth+1,maxdepth)