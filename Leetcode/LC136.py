"""
思路一： hash table 可行但有extra space
思路二： 按位异或，a,b,d,c,a,b,c   不管什么顺序，两个相同的元素例如a，a异或始终为0，剩下的d和0异或为d
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 
        
        res = 0
        for n in nums:
            res ^= n
        return res