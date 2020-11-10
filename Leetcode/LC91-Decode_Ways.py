"""
考验耐心， dp的问题
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        res = [0 for i in range(len(s))]
        s = s[::-1]
        if s[0] =='0':
            res[0] = 0
        else:
            res[0] = 1
            
        for i in range(1,len(s)):
            if s[i] == '0':
                res[i] = 0
                continue
            if i ==1 :
                if int(s[i]) >2:
                    res[i]= res[i-1]
                elif s[i] =='2':
                    if int(s[i-1])>6:
                        res[i] = res[i-1]
                    else:
                        res[i] = res[i-1] + 1
                elif s[i] =='1':
                    res[i] = res[i-1]+ 1
            if i>1:
                if int(s[i]) >2:
                    res[i]= res[i-1]
                elif s[i] =='2':
                    if int(s[i-1])>6:
                        res[i] = res[i-1]
                    else:
                        res[i] = res[i-1]+res[i-2]
                elif s[i] =='1':
                    res[i] = res[i-1]+res[i-2]
            
        return res[len(s)-1]