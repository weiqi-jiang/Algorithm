class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums,0,len(nums)-1)
    
        
        
        
    def helper(self, nums,left,right):
        mid = (left+right)//2
        if right == left:
            return nums[right]
        if right-left ==1:
            return min(nums[right],nums[left])

        if nums[left]<=nums[mid]<=nums[right]:
            return nums[left]
        if nums[mid]>nums[left] and nums[mid]>nums[right]:
            return self.helper(nums,mid+1,right)
        if nums[mid]<nums[left] and nums[mid]<nums[right]:
            return self.helper(nums,left,mid)