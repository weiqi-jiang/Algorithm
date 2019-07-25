class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput):
            return []
        if k <= 0:
            return [] 
        index = self.quickselect(tinput,k,0,len(tinput))
        return sorted(tinput[:index+1])
        
        
    def quickselect(self,nums,k,i,j):
        index = self._partition(nums,i,j)
        if index == k-1:
            return index
        elif index>k-1:
            return self.quickselect(nums,k,0,index)
        else:
            return self.quickselect(nums,k,index+1,len(nums))
        
        
    
    def _partition(self,nums,i,j):
        left,right = i,j-1
        low  = i
        while left<right:
            if nums[left]<nums[right]:
                nums[left],nums[low] = nums[low],nums[left]
                low+=1
            left+=1
        nums[right],nums[low] = nums[low],nums[right]
        return low