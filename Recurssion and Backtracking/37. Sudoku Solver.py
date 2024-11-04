def solveSudoku(self, board: List[List[str]]) -> None:
    def isvalid(ch,board,row,col):
        for i in range(9):
            if board[row][i]==ch:
                return False
            if board[i][col]==ch:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==ch:
                return False
        return True
    def solve(board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    for ch in "123456789":
                        if isvalid(ch,board,i,j):
                            board[i][j]=ch
                            if solve(board):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
    solve(board)