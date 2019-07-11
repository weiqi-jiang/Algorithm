#method 1

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