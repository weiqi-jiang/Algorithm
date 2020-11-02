"""
对于这种情况只能使用while loop 不能使用for loop
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        while i<len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)