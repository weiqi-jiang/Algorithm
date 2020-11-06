"""
dp题 lc62的变种
初始第一行第一列和LC62有区别
if isobstacle:
    path[0][j] = 0
else:
    path[0][j] = path[0][j-1]

if isobstacle:
    path[i][0] = 0
else:
    path[i][0] = path[i-1][0]    
    
    
    

if isobstacle:
    path[i][j] = 0
else:
    path[i][j] = path[i-1][j] + path[i][j-1]
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        path = [[0 for _ in range(n)]  for _ in range(m)]
        path[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        
        for i in range(1, n):
            if obstacleGrid[0][i] == 1:
                path[0][i] = 0
            else:
                path[0][i] = path[0][i-1]
                
        for j in range(1, m):
            if obstacleGrid[j][0] == 1:
                path[j][0] = 0
            else:
                path[j][0] = path[j-1][0]
                
        for p in range(m):
            for q in range(n):
                if obstacleGrid[p][q] == 1:
                    path[p][q] = 0
                else:
                    if p>=1 and q>=1:
                        path[p][q] = path[p-1][q] + path[p][q-1]
        return path[-1][-1]