class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickselect(nums,k)
        
        
        
    def quickselect(self,nums,k):
        if len(nums)<k:
            return -1
        
        index = self._partition(nums)
        if len(nums[index:]) == k:
            return nums[index] 
        elif len(nums[index:])>k:
            return self.quickselect(nums[index+1:],k)
        else:
            return self.quickselect(nums[:index],k-len(nums[index:]))
        
        
    def _partition(self,nums):
        pivot = nums[-1]
        left,right = 0,len(nums)-1
        low = left
        while left<right:
            if nums[left]<nums[right]:
                nums[left],nums[low] = nums[low],nums[left]
                low+=1
            left+=1
        nums[low],nums[right] = nums[right],nums[low]
        return low