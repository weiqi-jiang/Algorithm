class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        candidates = [i for i in range(len(nums))]
        for i in range(len(nums)):
            t = candidates[:]
            t.remove(i)
            self.helper(nums,i,[],res,t)
        
        return res
        
        
    def helper(self, nums,index,cur,res,candidates):
        '''
        candidate: 可供选择的index
        res 最终结果
        cur 之前保存的permuation
        index 当前选中的index
        '''
        if not candidates:
            cur.append(nums[index])
            res.append(cur)
            return 
        for cand in candidates:
            t = candidates[:]
            t.remove(cand)
            self.helper(nums,cand,cur+[nums[index]],res,t)