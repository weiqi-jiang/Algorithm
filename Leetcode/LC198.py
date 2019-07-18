class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        s = [0 for i in range(len(nums))]
        s[0] = nums[0]
        s[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            s[i] = max(s[i-2]+nums[i],s[i-1])
        return s[-1]