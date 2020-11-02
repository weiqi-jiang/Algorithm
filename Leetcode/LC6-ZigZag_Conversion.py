class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        if numRows ==1:
            return s
        for row in range(numRows):
            if row == 0 or row == numRows -1 :
                index = row
                while index<len(s):
                    res += s[index]
                    index += (numRows-1)*2
            else:
                step1,step2 = (numRows-1-row)*2,(row)*2
                flag ,index = 0, row
                while index<len(s):
                    res += s[index]
                    if flag ==0:
                        index += step1
                        flag = 1
                    else:
                        index += step2
                        flag = 0
        return res