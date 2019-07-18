class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n)    
        
    def helper(self,n):
        if n<5:
            return 0
        return n//5+ self.helper(n//5)