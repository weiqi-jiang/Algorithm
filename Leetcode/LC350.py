"""
思路很简单，双hash table，取共有key的最小value
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1, m2 = {}, {}
        for n in nums1:
            m1[n] = m1.get(n, 0) + 1
        for m in nums2:
            m2[m] = m2.get(m, 0) + 1
        
        result = []
        distinct_keys = set(list(m1.keys()) + list(m2.keys()))
        for k in m1:
            if k in m2:
                result += [k]*min(m1[k], m2[k])
        return result