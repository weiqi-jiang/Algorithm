class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        
        s = str.strip(" ")
        if not str:
            return 0 
        sign = 1
        res = ""
        for i in range(len(s)):
            if i ==0: 
                if s[i]=="-":
                    sign = -1
                    continue
                if s[i] == "+":
                    sign = 1
                    continue
            if s[i].isdigit():
                res += s[i]
            else:
                break
        if res:
            if sign*int(res)>INT_MAX:
                return INT_MAX
            if sign*int(res)<INT_MIN:
                return INT_MIN
            return sign*int(res)
        return 0
        