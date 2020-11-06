"""
dp题 
初始第一行第一列的path数都为1 
path[i][j] = path[i-1][j] + path[i][j-1]
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for i in range(n)] for i in range(m)]
        path[0] = [1 for _ in range(n)]
        for i in range(len(path)):
            path[i][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i>=1 and j>=1:
                    path[i][j] += path[i-1][j] + path[i][j-1]
        return path[-1][-1]