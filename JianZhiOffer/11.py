# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent<=0:
            if base:
                return 1/self.helper(base,-exponent)
            else:
                print('divided by zero')
                return 
        else:
            return self.helper(base,exponent)
            
    def helper(self,base,exponent):
        if exponent == 0 :
            return 1
        if exponent == 1:
            return base
        if exponent%2 == 1:
            res = self.helper(base,int(exponent/2))
            return res**2*base
        else:
            res = self.helper(base,int((exponent-1)/2))
            return res**2