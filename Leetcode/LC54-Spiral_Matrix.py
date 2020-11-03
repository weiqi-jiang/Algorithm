"""
steps:
1. 第一行全部extend
2. pop 每一行的最后一个元素
3. pop 最后一行，需要先倒序
4. pop 每一行的第一个元素 
注意每次都需要判断当前matrix是否还有元素没有处理，不然容易出错
"""

class Solution(object):
    def spiralOrder(self, matrix):
        arr = []
        while matrix:
            #extend the top row
            arr.extend(matrix.pop(0))
            #extend the right colomn
            if matrix:
                for i in range(len(matrix)):
                    if matrix[i]:
                        arr.append(matrix[i].pop())
            #extend the bottom row
            if matrix:
                arr.extend(matrix.pop()[::-1])
            #extend the left colomn
            if matrix:
                for i in range(len(matrix)-1,-1,-1):
                    if matrix[i]:
                        arr.append(matrix[i].pop(0))
        return arr
		

#method 2
"""
用一个matrix去记录当前点是否访问到了

但这个题的精髓在于check=2
如果不加check 就会一直在while loop中跳不出来
加check=1 也不行，绕完一圈 check-=1 就跳出了，需要让他再绕一圈去确定没有可以迭代的了。
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        up,down,left,right = 0,0,0,1
        
        status = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        all_elements = len(matrix)*len(matrix[0])
        res = []
        self.helper(status,matrix,0,0,up,down,left,right,res,all_elements)
        return res
        
        
    def helper(self,status,matrix,i,j,up,down,left,right,res,count):
        
        res.append(matrix[i][j])
        status[i][j]=1
        check = 2
        while check:
            if right:
                if j <len(matrix[0])-1 and status[i][j+1]==0:
                    self.helper(status,matrix,i,j+1,up,down,left,right,res,count)
                else:
                    right,down = 0,1

            if down:
                if i <len(matrix)-1 and status[i+1][j]==0:
                    self.helper(status,matrix,i+1,j,up,down,left,right,res,count)
                else:
                    down,left = 0,1

            if left:
                if j >0 and status[i][j-1]==0:
                    self.helper(status,matrix,i,j-1,up,down,left,right,res,count)
                else:
                    left,up = 0,1

            if up:
                if i >0 and status[i-1][j]==0:
                    self.helper(status,matrix,i-1,j,up,down,left,right,res,count)
                else:
                    up,right = 0,1
            check -=1