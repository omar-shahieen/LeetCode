class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        zero_rows =set()
        zero_cols = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 :
                    zero_rows.add(i)
                    zero_cols.add(j)

        for zero_row in zero_rows:
            for j in range(n):
                matrix[zero_row][j]= 0
        for zero_col in zero_cols:
            for i in range(m):
                matrix[i][zero_col]= 0
        
                    

