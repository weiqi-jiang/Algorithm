# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
recursive approach
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def helper(root, res):
            if root.left:
                helper(root.left, res)
            res.append(root.val)
            if root.right:
                helper(root.right,res)
        
        res = []
        helper(root,res)
        return res
            


"""
iterative approach
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res,s = [],[]
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                return res
            node = s.pop()
            res.append(node.val)
            root = node.right