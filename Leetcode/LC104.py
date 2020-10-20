"""
recursively 的思路
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        maxdepth = [0]
        self.helper(root,1,maxdepth)
        return maxdepth[-1]
        
    def helper(self,root,depth,maxdepth):
        maxdepth[-1] = max(maxdepth[-1],depth)
        if root.left:
            self.helper(root.left,depth+1,maxdepth)
        if root.right:
            self.helper(root.right,depth+1,maxdepth)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
iteratively 的思路
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        def helper(candidate, res):
            while candidate:
                node, depth = candidate.pop(0)
                res.append(depth)
                if node.left:
                    candidate.append((node.left, depth+1))
                if node.right:
                    candidate.append((node.right, depth+1))
        if not root:
            return 0
        res = []
        helper([(root,1)],res)
        return max(res)