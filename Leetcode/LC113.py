    def dfs(self,curpath,res,root,add,sum):
        if not root:
            return 
        add+=root.val
        if not root.left and not root.right:
            if add == sum:
                curpath.append(root.val)
                res.append(curpath)
            return 
        if root.left:
            self.dfs(curpath+[root.val],res,root.left,add,sum)
        if root.right:
            self.dfs(curpath+[root.val],res,root.right,add,sum)