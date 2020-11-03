"""
一个DP问题，不应该只是easy的难度

到index为n未知的最大和表示为max_sum(n)
max_sum(n) = max(cur_element(n), max_sum(n-1))
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)