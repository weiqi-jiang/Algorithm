"""
LC39的变种
有两个要点
1. unique  如果candidate 中有重复 1 7 1 target = 8 就会有[1 7] [7 1]两种
2. 每个num只能用一次 但是如果有两个一模一样的就可以有多从
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        for i in range(len(candidates)):
            self.helper(candidates,target,[candidates[i]],res,i,0)
        return res
        
    def helper(self,candidates,target,cur,res,index,add):
        '''
        cur : 之前已有的输入
        index 当前num
        '''
        add += candidates[index]
        if add>target:
            return 
        if add==target:
            if cur not in res:
                res.append(cur)
        else:
            for i in range(index+1, len(candidates)): 
                if i-index>1 and candidates[i]==candidates[i-1]:
                    continue
                self.helper(candidates,target,cur+[candidates[i]],res,i,add)
                