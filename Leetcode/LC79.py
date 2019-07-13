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
        temp = board[i][j]
        board[i][j] = '%'
        res = self.dfs(board,i+1,j,remain[1:]) or self.dfs(board,i-1,j,remain[1:]) or self.dfs(board,i,j+1,remain[1:]) or self.dfs(board,i,j-1,remain[1:])
        board[i][j] = temp
        return res