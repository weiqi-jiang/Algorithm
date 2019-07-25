class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        self.mirrorTree(root)
        
        
    def mirrorTree(self,root):
        if not root:
            return 
        root.left,root.right = root.right,root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root