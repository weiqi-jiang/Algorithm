"""
自下而上
1. root.left and root.right -> 把左节点按照题目要求的形式插到root和右节点之间，返回root 和right
也就是当前这个局部linked list的两端
2. root.left and not root.right ->把左节点移到右边去，返回root和right
3. root.right and not root.left -> 返回root 和right 
4. not root.right and not root.left -> return root, root
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        root,_ = self.helper(root)
       
        
        
    def helper(self,root):
        
        if not root.left and not root.right:
            return root,root
        if root.left and root.right:
            leftfirst,leftlast = self.helper(root.left)
            rightfirst,rightlast  =self.helper(root.right)
            root.right = leftfirst
            root.left = None
            leftlast.right = rightfirst
            return root,rightlast
        if root.left and not root.right:
            leftfirst,leftlast = self.helper(root.left)
            root.right = leftfirst
            root.left = None
            return root,leftlast
        if root.right and not root.left:
            rightfirst,rightlast  =self.helper(root.right)
            return root,rightlast