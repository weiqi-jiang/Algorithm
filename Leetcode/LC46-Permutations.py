"""
标准全排列
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(candidates, res, cur):
        """
        candidates  当前剩下没有使用的元素
        res 用来保存最终结果
        cur 当前permutations
        """
            if not candidates:
                res.append(cur)
                return 
            for i in range(len(candidates)):
                integers = candidates[i]
                helper(candidates[:i] + candidates[i+1:], res, cur+[integers])
        
        res = []
        helper(nums[:], res, [])
        return res
            