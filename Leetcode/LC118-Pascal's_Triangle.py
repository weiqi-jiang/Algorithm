"""
类似于DP的一种解法
一层一层的算
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        if numRows  == 1:
            return [[1]]
        if numRows ==2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        while len(res)<numRows:
            cur = [1]
            lastlevel = res[-1]
            i,j = 0,1
            while j<=len(lastlevel)-1:
                cur.append(lastlevel[i]+lastlevel[j])
                i+=1
                j+=1
            cur.append(1)
            res.append(cur)
        return res