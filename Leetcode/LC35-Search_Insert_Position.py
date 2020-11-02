"""
遍历，当前元素大于等于target 都可以返回index i
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 
        for i in range(len(nums)):
            if nums[i]>= target :
                return i 
        return len(nums)