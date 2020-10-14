"""
思路一： sorting  O（NlogN）
思路二： hash map O(N) 
"""
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        tmp = {}
        for i in range(len(nums)):
            if nums[i] not in tmp:
                tmp[nums[i]] = 1
            else:
                return True
        return False