"""
判断是否是回文依然是经典的two pointer
这个题只是在回文判断的基础上加上了 在不转string的前提下，怎么提取每一位数字
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = []
        while x>=10:
            n.append(x%10)
            x = x//10
        n.append(x)
        p1,p2 = 0,len(n)-1
        while p1 <= p2:
            if n[p1] != n[p2]:
                return False 
            else:
                p1+=1
                p2-=1
        return True