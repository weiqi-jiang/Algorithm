# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
recursively 
"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left,right):
            if (not left) and (not right):
                return True
            elif not left and right:
                return False
            elif right and not left:
                return False 
            elif left and right:
                if left.val != right.val:
                    return False
                else:
                    return helper(left.right, right.left) and helper(left.left, right.right)
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