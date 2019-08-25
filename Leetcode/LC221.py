class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = int(matrix[0][0])
        stat = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                stat[0][i] = 1
                res = 1
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                stat[i][0] = 1
                res = 1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '1':
                    stat[i][j] = min(stat[i-1][j],stat[i][j-1],stat[i-1][j-1])+1
                    res = max(res,stat[i][j])
        return res**2