# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
recursively 的解法，不太容易想，但也不至于很难
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if (not node1 and node2) or (not node2 and node1):
                return False
            if node1.val != node2.val:
                return False 

            return helper(node1.left, node2.right) and helper(node1.right, node2.left)
        return helper(root,root)

"""
iteratively 的思路，和recursively 其实差不多的思想
"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        candidate = [(root,root)]
        while candidate:
            p,q = candidate.pop(0)
            if (not p and q) or (not q and p):
                return False 
            if p and q and p.val!=q.val:
                return False
            if p and q:
                candidate.append((p.left, q.right))
                candidate.append((p.right, q.left))
        return True