"""
recursive approach
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def helper(root, res):
            if not root:
                return 
            res.append(root.val)
            helper(root.left, res)
            helper(root.right,res)
        helper(root,res)
        return res
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                ret.append(node.val)
                stack.append(node.left)
        return ret