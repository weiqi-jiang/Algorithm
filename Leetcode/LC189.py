class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        
        step = k%len(nums)
        bp = len(nums)-step
        if step:
            t1 = nums[:bp]
            t2 = nums[bp:]
            nums[:step] = t2
            nums[step:] = t1