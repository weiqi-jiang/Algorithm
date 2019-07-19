class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        v= [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        count =0
        def dfs(grid,i,j,v):
            v[i][j] = 1
            if i<len(grid)-1 and v[i+1][j]==0 and grid[i+1][j]=='1':
                dfs(grid,i+1,j,v)
            if i>0 and v[i-1][j]==0 and grid[i-1][j]=='1':
                dfs(grid,i-1,j,v)
            if j<len(grid[0])-1 and v[i][j+1]==0 and grid[i][j+1]=='1':
                dfs(grid,i,j+1,v)
            if j>0 and v[i][j-1]==0 and grid[i][j-1]=='1':
                dfs(grid,i,j-1,v)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== '1' and v[i][j]==0:
                    dfs(grid,i,j,v)
                    count+=1
        return count