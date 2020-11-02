"""
传统递归问题
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(candidates)):
            self.helper(candidates,target,[candidates[i]],res,i)
        return res
        
    def helper(self,candidates,target,cur,res,index):
        '''
        cur : 之前已有的输入
        index 当前num
        '''
        
        if sum(cur)>target:
            return 
        if sum(cur)==target:
            res.append(cur)
        else:
            for i in range(index, len(candidates)): 
                self.helper(candidates,target,cur+[candidates[i]],res,i)
                