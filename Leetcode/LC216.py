class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        numbers = [ i for i in range(1,10)]
        self.dfs(k,n,0,[],res,numbers)
        return res
        
    def dfs(self,k,target,index,cur,res,numbers):
        if k<0 or target<0:
            return 
        elif k ==0 and target ==0:
            res.append(cur)
        elif index<len(numbers) and numbers[index]*k>target:
            return 
        else:
            for i in range(index,len(numbers)):
                self.dfs(k-1,target-numbers[i],i+1,cur+[numbers[i]],res,numbers)
		
		
		
		
		
		
 