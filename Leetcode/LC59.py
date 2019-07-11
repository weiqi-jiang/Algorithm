class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        candidates = [i for i in range(1,n**2+1)]
        res = [[0 for i in range(n)] for i in range(n)]
        visited= [[0 for i in range(n)] for j in range(n)]
        # init the first num
        i,j = 0,0
        res[0][0] = candidates.pop(0)
        visited[0][0]=1
        while candidates:
            # going right
            while candidates and j<n-1 and visited[i][j+1]==0:
                j+=1
                res[i][j] = candidates.pop(0)
                visited[i][j]=1
            #going down
            while candidates and i<n-1 and visited[i+1][j]==0:
                i+=1
                res[i][j] = candidates.pop(0)
                visited[i][j]=1
            #going left
            while candidates and j>0 and visited[i][j-1]==0:
                j-=1
                res[i][j] = candidates.pop(0)
                visited[i][j]=1
            #going up
            while candidates and i>0 and visited[i-1][j]==0:
                i-=1
                res[i][j] = candidates.pop(0)
                visited[i][j]=1
        return res