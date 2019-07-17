class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        marginNode = []
        visited = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i ==0 or i == len(board)-1 or j ==0 or j == len(board[0])-1) and board[i][j] == 'O':
                    marginNode.append((i,j))
                    
        
        keep = [] 
        
        while marginNode:
            curi,curj = marginNode.pop(0)
            keep.append((curi,curj))
            visited[curi][curj] = 1
            if curi>0 and board[curi-1][curj]=='O' and visited[curi-1][curj] ==0:
                marginNode.append((curi-1,curj))
            if curi<len(board)-1 and board[curi+1][curj]=='O' and visited[curi+1][curj] ==0:
                marginNode.append((curi+1,curj))
            if curj>0 and board[curi][curj-1]=='O' and visited[curi][curj-1] ==0:
                marginNode.append((curi,curj-1))
            if curj<len(board[0])-1 and board[curi][curj+1]=='O' and visited[curi][curj+1] ==0:
                marginNode.append((curi,curj+1))
        for i,j in keep:
            board[i][j] = 'k'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'k':
                    board[i][j] = 'O'
                else:
                    if board[i][j] == 'O':
                        board[i][j] = 'X'