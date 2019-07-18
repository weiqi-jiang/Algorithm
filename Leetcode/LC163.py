class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
    
        if not nums:
            return None
        if len(nums)==1:
            return 0
        return self.find(nums,0,len(nums)-1)
    
    def find(self,nums,left,right):
        while left<right:
            if left+1 ==right:
                if nums[left]>nums[right]:
                    return left
                else:
                    return right
            mid = (left+right)//2

            if nums[mid]<nums[mid+1]:
                left = mid 
            else:
                right = mid