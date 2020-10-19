"""
思路没有说的，注意.intersection的用法即可
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1, m2 = {}, {}
        for n in nums1:
            m1[n] = m1.get(n, 0) + 1
        for m in nums2:
            m2[m] = m2.get(m, 0) + 1
        
        a = set(m1.keys())
        b = set(m2.keys())
        
        return list(a.intersection(b))