class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre  or not tin:
            return None
        return self.helper(pre,tin)
        
        
    def helper(self,pre,tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        index = tin.index(pre[0])
        left = tin[:index]
        right = tin[index+1:]
        root.left = self.helper(pre[1:len(left)+1], left)
        root.right = self.helper(pre[len(left)+1:], right)
        return root