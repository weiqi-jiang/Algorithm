class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
        
        
        
        
    def helper(self,nums):
        if not nums:
            return 0
        if len(nums) <=2:
            return max(nums)
        money = [0 for i in range(len(nums))]
        money[0] = nums[0]
        money[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            money[i] = max(nums[i] + money[i-2],money[i-1])
        return money[-1]