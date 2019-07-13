class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        res = [[]]
        for length in range(1,len(nums)+1):
            for i in range(len(nums)):
                self.subset(length,[],res,nums,i,0)
        return res
        
        
    def subset(self,length,cur,res,nums,index,count):

        temp =cur+[nums[index]]
        count+=1
        if count == length:
            res.append(temp)
            return
        else:
            if index == len(nums)-1:
                return
            for i in range(index+1,len(nums)):
                self.subset(length,temp,res,nums,i,count)