class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]].append(i)
            else:
                m[s[i]] = [i]
                
        res = len(s)
        for k in m:
            if len(m[k]) == 1:
                res = min(res, m[k][0])
        return res if res<len(s) else -1 
