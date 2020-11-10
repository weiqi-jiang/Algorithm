"""
Backtracking 题目， 限制一下元素的长度即可，同时注意到输出是combinations不是
permutation 所以顺序不同的结果是相同的
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(nums, limits, cur, res):
            if len(cur)==limits:
                res.append(cur)
                return 
            if not nums:
                return 
            else:
                for i in range(len(nums)):
                    helper(nums[i+1:], limits, cur+[nums[i]], res)
        
        res = []
        helper([i for i in range(1,n+1)], k, [], res)
        return res
        