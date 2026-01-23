class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        walk through the edges if you can reach any 'o' from the edge replace with'#'
        after that walk through all the grapgh and replace # with o and o with X
        """
        if not board or not board[0]:
            return


        n= len(board)
        m = len(board[0])


        def dfs(i , j):
            if i < 0 or j < 0 or i >= n or j >= m :
                return 
            if board[i][j] == 'O' :
                 board[i][j] = '#'
            else :
                return 

            for di , dj in [(1,0) , (-1,0) , (0,1) , (0,-1)]:
                dfs(i + di , j + dj )

        # first and last col
        for i in range(n):
            dfs(i , 0)
            dfs(i, m-1)


        # first and last row
        for j in range(m):
            dfs(0,j)
            dfs(n-1,j)

        # Flip captured regions and restore border-connected regions
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' : # surrounded
                    board[i][j] = 'X'
                elif board[i][j] == '#': # border connected
                    board[i][j] = 'O'

        