class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        r1 = self.round(n)
        r2 = self.round(r1)
        while True:
            if r1 == 1:
                return True
            if r1==r2:
                return False
            else:
                r1 = self.round(r1)
                r2 = self.round(self.round(r2))
        
        
    def round(self,n):
        result = 0
        while n:
            result += (n%10)**2 
            n = n//10
        return result