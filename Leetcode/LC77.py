class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = [i for i in range(1,n+1)]
        res = []
        for i in range(len(nums)):
            self.combination(k,[],res,0,nums,i)
        
        return res
        
        
    def combination(self,max_element,cur,res,count,nums,index):
        temp = cur+[nums[index]]
        count += 1
        if count == max_element:
            res.append(temp)
            
        else:
            for i in range(index+1,len(nums)):
                self.combination(max_element,temp,res,count,nums,i)