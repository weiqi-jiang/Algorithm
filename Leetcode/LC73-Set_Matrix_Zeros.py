"""
主要考察空间复杂度 
SC O(M+N)
ituitive solution
记录包含0的行和列，然后分别置零

"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        for row in zero_row:
            matrix[row] = [0]* len(matrix[row])
        for col in zero_col:
            for i in range(len(matrix)):
                matrix[i][col] = 0

"""
Optimized solution 
SC O(1)
不适用额外的空间来记录0值包含的行和列，使用matrix本身
如果matrix[i][j] == 0  我们就把matrix[0][j] matrix[i][0] 也就是每行每列的首元素置0，
这样既保留了信息而且该0值不会对后来的判断造成影响
"""
