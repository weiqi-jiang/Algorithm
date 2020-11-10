# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
递归， 和二分法的含义差不多
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(nums):
            if len(nums)==0:
                return None
            if len(nums)==1:
                return TreeNode(nums[-1])
        
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            left ,right = helper(nums[:mid]), helper(nums[mid+1:])
            node.left = left 
            node.right = right
            return node 
        return helper(nums)