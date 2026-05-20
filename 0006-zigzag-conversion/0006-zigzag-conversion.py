class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if  numRows == 1 :
            return s 
        cols = len(s)
        table = [['$' for _ in range(cols)] for _ in range(numRows)]
        i = 0 
        down =True
        for j in range(cols):
            table[i][j] = s[j]
            if i == numRows -1 :
                down =False
            if i == 0 :
                down = True
            i = i+1 if down else i-1



        res = []
        for i in range(numRows):
            for j in range(cols):
                if table[i][j] != '$':
                    res.append(table[i][j])

        return "".join(res)

        