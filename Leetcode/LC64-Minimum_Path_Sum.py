"""
lc62 63 64都是一个类型 标准的dp题目
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        path[0] = grid[0]
        for i in range(0, len(grid[0])):
            if i>=1:
                path[0][i] += path[0][i-1]
        for j in range(0,len(grid)):
            if j >= 1:
                path[j][0] = grid[j][0] + path[j-1][0]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i>0 and j>0:
                    path[i][j] = min(path[i][j-1] , path[i-1][j]) + grid[i][j]
        return path[-1][-1]