class Solution:
    def totalNQueens(self, n: int) -> int:
        self.solutions = 0 

        dig1 = set() # r+ c  -> / 
        dig2 = set() # r - c -> \ 
        cols = set()

        def backtrack(r ):
            if r == n :
                self.solutions += 1
                return 


            for c in range(n):


                if c in cols or r-c in dig2 or r+c in dig1  :
                    continue 

                dig1.add(r+c)
                dig2.add(r-c)
                cols.add(c)

                backtrack(r+1)

                
                dig1.remove(r+c)
                dig2.remove(r-c)
                cols.remove(c)

        backtrack(0)
        return self.solutions