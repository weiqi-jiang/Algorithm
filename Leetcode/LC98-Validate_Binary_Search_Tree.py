"""
recursively 的思路，重点在于需要更新low 和high， 不能简单的判断当前node和子节点是否满足BST，还要考虑上一级
"""
class Solution:
	def isValidBST(self, root: TreeNode) -> bool:
		def helper(self,low,high,root):
			if not root:
				return True
			if root.val<=low or root.val>=high:
				return False
			return self.helper(low,root.val,root.left) and self.helper(root.val,high,root.right)
		
		low = -float('inf')
		high = float('inf')
		return self.helper(low,high,root)
		
		
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
BST 的中序遍历结果是ordered， i<i+1 如果出现任意i>=i+1则bst不成立
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inorder(root,vals):
            if not root:
                return 
            inorder(root.left, vals)
            vals.append(root.val)
            inorder(root.right, vals)
        
        def judge(vals):
            if len(vals) <=1:
                return True
            for i in range(len(vals)-1):
                if vals[i]>=vals[i+1]:
                    return False 
            return True 
        
        vals = []
        inorder(root,vals)
        return judge(vals)
                