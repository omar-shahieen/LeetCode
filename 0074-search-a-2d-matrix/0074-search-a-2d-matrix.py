class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top , bottom = 0 , len(matrix) - 1

        row = -1 
        while top <= bottom :
            mid = top + (bottom - top) // 2

            if matrix[mid][0] == target :
                return True
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else :
                top =  mid + 1  
                row = mid       

        l , r = 0 , len(matrix[0]) - 1

        while l <= r :
            m = l + (r-l)//2
            if matrix[row][m] == target :
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else :
                l = m + 1
        
        return False
