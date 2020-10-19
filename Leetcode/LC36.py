"""
没有什么讨巧的  按照规则去查就行
"""
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            if not self.checkrow(board,i) or not self.checkcol(board,i):
                return False
        for i in range(3):
            for j in range(3):
                if not self.check33(board,i*3,j*3):
                    return False
        return True
        
    def checkrow(self,board,i):
        m = {}
        for n in board[i]:
            if n!='.':
                n = int(n)
                if n>9 or n<1:
                    return False
                if n not in m:
                    m[n]=1
                else:
                    return False
        return True
    
    def checkcol(self,board,i):
        col = [ board[j][i] for j in range(len(board))]
        m = {}
        for n in col:
            if n!='.':
                n = int(n)
                if n>9 or n<1:
                    return False
                if n not in m:
                    m[n]=1
                else:
                    return False
        return True
    
    def check33(self,board,p,q):
        m = {}
        for i in range(p,p+3):
            for j in range(q,q+3):
                if board[i][j]!='.':
                    n = int(board[i][j])
                    if n>9 or n<1:
                        return False
                    if n not in m:
                        m[n]=1
                    else:
                        return False
        return True
                    