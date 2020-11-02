"""
先binary search找到任一一个目标元素
然后以该元素为中心向两边找
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        index = self.binarySearch(nums,target)
        if index ==-1:
            return [-1,-1]
        else:
            left,right = index,index
            while left>=0 and nums[left] == nums[index]:
                left-=1
            while right<=len(nums)-1 and nums[right] == nums[index]:
                right+=1
            return [left+1,right-1]
                
      
    def binarySearch(self,nums,target):
        left,right = 0, len(nums)-1
        while left<=right:
            
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid +1
        return -1