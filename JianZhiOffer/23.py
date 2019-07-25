class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        
        queue,res = [root],[]
        while queue:
            curnode = queue.pop(0)
            res.append(curnode.val)
            if curnode.left:
                queue.append(curnode.left)
            if curnode.right:
                queue.append(curnode.right)
        return res