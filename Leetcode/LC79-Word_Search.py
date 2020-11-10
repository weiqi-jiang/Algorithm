"""
思路： dfs ，用矩阵来记录当前元素是否被访问
难点在于如果word是abcd 在c旁边有两个d，这个时候不能共用一个visit矩阵
需要递归的时候传入临时visit矩阵
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word):
                    return True
        return False
        
        
        
        
    def dfs(self, board, i,j, remain):
        '''
        remain： characters which are remained to be found
        '''
        if not remain:
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or remain[0]!= board[i][j]:
            return False
        ## 这一部分是核心思想
        temp = board[i][j]
        board[i][j] = '%'
        res = self.dfs(board,i+1,j,remain[1:]) or self.dfs(board,i-1,j,remain[1:]) or self.dfs(board,i,j+1,remain[1:]) or self.dfs(board,i,j-1,remain[1:])
        board[i][j] = temp
        ##
        return res