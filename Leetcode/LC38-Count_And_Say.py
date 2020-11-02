"""
按照规则去做
先说个数再说数字 比如 111 就是31 three one
12 就是 11 12 one one| one two
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==1 :
            return "1"
        res = ['1']
        m = 1
        while m<=n:
            count = res[-1]
            tmp  = self.countANDsay(count)
            res.append(tmp)
            m+=1
        return res[n-1]
            
            
    def countANDsay(self,s):
        res = ''
        temp = s[0]
        c = 0
        for i  in range(len(s)):
            if s[i] == temp:
                c += 1
            else:
                res += (str(c)+temp)
                temp = s[i]
                c = 1
        res += (str(c)+temp)
        return res