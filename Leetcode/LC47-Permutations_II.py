"""
BP 问题
在LC46的基础上改进
优化点在于每次递归的时候不是选择每个元素，而是选择unique元素
"""
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        nums.sort()
        self.dfs(nums,[],result)
        return result
    
    def dfs(self,nums,permutation,result):
        if len(nums)==0:
            result.append(permutation)
        else:
            for i in range(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:
                    continue
                else:
                    self.dfs(nums[:i]+nums[i+1:],permutation+[nums[i]],result)
            