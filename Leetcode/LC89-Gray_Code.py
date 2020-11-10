class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [[0,1]]
        res.append([0,1,3,2])
        if 0<n <=2:
            return res[n-1] 
        if n <=0:
            return [0]
        for i in range(2,n):
            res.append(res[i-1]+ [2**(i) + p for p in res[i-1][::-1]])
        return res[n-1]