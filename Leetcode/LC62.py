class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        status = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            status[i][0] = 1
        for j in range(n):
            status[0][j] = 1
            
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    status[i][j] = status[i][j-1] + status[i-1][j]
        return status[m-1][n-1]