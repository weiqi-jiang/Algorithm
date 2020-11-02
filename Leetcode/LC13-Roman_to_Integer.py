"""
翻译每个字符对应的数字，一种特殊情况，高价值字符前面有一个低价值字符的时候
低价值字符以负数形式翻译，然后求和。
"""
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = []
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1):
            if d[s[i]]<d[s[i+1]]:
                t.append(-d[s[i]])
            else:
                t.append(d[s[i]])
        t.append(d[s[-1]])
        return sum(t)