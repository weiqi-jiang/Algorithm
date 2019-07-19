class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.dfs(root)
        
        
    def dfs(self,root):
        curmaxdeep = 0
        res  =[]
        stack = [(root,1)]
        while stack:
            
            node, depth = stack.pop()
            if depth > curmaxdeep:
                curmaxdeep = depth
                res.append(node.val)
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
        return res
            