class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def dfs(i,j):
            row = set()
            col = set()
            grid = set()
            for k in range(9):
                if board[k][j] in col : 
                    return False
                elif board[k][j] != '.' :
                    col.add(board[k][j])

                if board[i][k] in row : 
                    return False
                elif  board[i][k] != '.':
                    row.add(board[i][k])

            shiftRow = i//3
            shiftCol = j//3
            for u in range(shiftRow * 3 , (shiftRow+1) *3):
                for v in range(shiftCol * 3 , (shiftCol+1) *3): 
                    if board[u][v] in grid : 
                        return False
                    elif  board[u][v] != '.':
                        grid.add(board[u][v])

            return True

        for i in range (9):
            for j in range(9):
                if not dfs(i,j):
                    return False

        return True
            



                
        