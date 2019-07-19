class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s or not t:
            return True
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            if s[i] not in m1:
                m1[s[i]] = [i]
            else:
                m1[s[i]].append(i)
        for i in range(len(t)):
            if t[i] not in m2:
                m2[t[i]] = [i]
            else:
                m2[t[i]].append(i)
        v1,v2 = m1.values(),m2.values()
        for v in v1:
            if not v in v2:
                return False
        return True