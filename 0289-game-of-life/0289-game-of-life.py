class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        lastState  = copy.deepcopy(board)
        m = len(board)
        n = len(board[0])

        def countLive(i , j ):

            live = 0 
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue

                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        live += lastState[ni][nj] == 1

            return live
            

        for i in range(m):
            for j in range(n):
                live = countLive(i,j)
                if lastState[i][j] == 1:
                    if live > 3 or live < 2 :
                        board[i][j] = 0

                else:
                    if live == 3 :
                        board[i][j] = 1

