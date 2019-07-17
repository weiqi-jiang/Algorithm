class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.build(nums)
        
    def build(self,nums):
        if not nums:
            return None
        rootindex = len(nums)//2
        root = TreeNode(nums[rootindex])
        root.left = self.build(nums[:rootindex])
        root.right = self.build(nums[rootindex+1:])
        return root
    