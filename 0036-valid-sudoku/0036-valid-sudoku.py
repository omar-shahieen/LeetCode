class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for i in range (9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                gridIdx = j//3 + (i//3)*3
                if num  in rows[i] or num in cols[j] or num in grids[gridIdx]:
                    return False
                rows[i].add(num)   
                cols[j].add(num)   
                grids[gridIdx].add(num)   


        return True
            



                
        