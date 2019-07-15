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