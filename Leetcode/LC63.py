class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        
        status = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        else:
            status[0][0]=1
            
        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                status[i][0] += status[i-1][0]
        for j in range(1,n):
            if obstacleGrid[0][j] == 0:
                status[0][j] += status[0][j-1]
            
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    if obstacleGrid[i][j]==0:
                        status[i][j] = status[i][j-1] + status[i-1][j]
                    
        return status[m-1][n-1]