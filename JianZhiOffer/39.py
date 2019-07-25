# iterative
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue = [(pRoot,1)]
        treedepth = 0
        while queue:
            curnode,curdepth = queue.pop()
            treedepth = max(treedepth,curdepth)
            if curnode.left:
                queue.append((curnode.left,curdepth+1))
            if curnode.right:
                queue.append((curnode.right,curdepth+1))
        return treedepth