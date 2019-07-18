class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = {}
        for i in range(len(s)-9):
            pattern = s[i:i+10]
            if not res.get(pattern):
                res[pattern] = 1
            else:
                res[pattern] += 1
        return [ k for k,v in res.items() if v>1   ] 