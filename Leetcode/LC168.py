class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.helper(n)
        
    def helper(self,n):
        res = []
        while n>0:
            res.append((n-1)%26)
            n = (n-1)//26
        
        res = [chr(ord('A')+n) for n in res]
        return ''.join(res)[::-1]