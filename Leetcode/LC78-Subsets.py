"""
ituitive solution
在LC77的基础上 遍历每种长度，找到该长度下所有可能的subset
但是会有很多重复计算
"""
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
"""
更优化的想法
总是保存当前cur
记录当前的index，只遍历index后的元素，保证完备，遍历到了所有长度
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        res = []

        self.subset([],res,nums,0)
        return res
        
        
    def subset(self,cur,res,nums,index):

        res.append(cur)
        for i in range(index,len(nums)):

            self.subset(cur+[nums[i]],res,nums,i+1)