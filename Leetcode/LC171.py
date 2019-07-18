class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            num = ord(s[i])-ord('A')+1
            res = 26*res + num
        return res