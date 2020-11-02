"""
思路：这个题主要难点有两个，一个是index的map func要找到，另一个是怎么在变化过程中保留原图像元素不变
代码是强行把元素变为2维，一维用来保留原来的元素，另一维用做变换，完成后去掉第一维。当然也可以复制图像
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = [matrix[i][j],0]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][len(matrix)-1-i][1] = matrix[i][j][0]
            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = matrix[i][j][1]