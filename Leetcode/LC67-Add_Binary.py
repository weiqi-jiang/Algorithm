"""
老老实实 merge思路
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        p1,p2 = 0,0
        res = []
        flag = 0
        while p1<len(a) and p2<len(b):
            cur_value = int(a[p1])+ int(b[p2]) + flag
            if cur_value >=2:
                cur_value -= 2
                flag=1
            else:
                flag=0
            p1+=1
            p2+=1
            res.append(str(cur_value))
        while p1 < len(a):
            cur_value = int(a[p1])+ flag
            if cur_value >=2:
                cur_value -= 2
                flag=1
            else:
                flag=0
            p1+=1
            res.append(str(cur_value))
            
        while p2 < len(b):
            cur_value = int(b[p2]) + flag
            if cur_value >=2:
                cur_value -= 2
                flag=1
            else:
                flag=0
            p2+=1
            res.append(str(cur_value))
        if flag:
            res.append('1')
        return ''.join(res)[::-1]

"""
利用python现成的一些函数
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        return str(bin(a+b))[2:]
        
            