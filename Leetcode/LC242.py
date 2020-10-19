"""
同样的字母和数量 不同的顺序，  注意都为空时和两者相同时 为True
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t :
            return True
        
        if len(s)!=len(t):
            return False 
        if set(s) != set(t):
            return False 
        if s==t:
            return True
        
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            if s[i] in m1:
                m1[s[i]] += 1
            else:
                m1[s[i]] = 1
            
            if t[i] in m2:
                m2[t[i]] += 1
            else:
                m2[t[i]] = 1
        
        for k in m1:
            if m1[k] != m2[k]:
                return False
        return True
