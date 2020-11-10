"""
在subsets 的基础上加上一层过滤就行
如果nums[i] == nums[i-1] continue 但同时nums[index]本身会递归一次
所有不会出现不完备的情况 
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return 
        res = []
        nums.sort()
        self.subset([],res,nums,0)
        return res
        
        
    def subset(self,cur,res,nums,index):

        res.append(cur)
        for i in range(index,len(nums)):
            if i>index and nums[i] == nums[i-1]:
                continue
            self.subset(cur+[nums[i]],res,nums,i+1)