class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [ ]
        def solve(path , l , r):
            if l == n and r ==n:
                res.append(path)

            if l < n : 
                solve(path + '(' , l+1 ,r )
            if l > r :
                solve(path + ')' , l , r +1 )

        solve("" ,0 ,0)
        return res
             
        