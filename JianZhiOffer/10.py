class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n<0:
            n = n&0xffffffff
        while n:
            n = n&(n-1)
            count+=1
        return count