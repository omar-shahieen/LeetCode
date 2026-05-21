class Solution:
    def romanToInt(self, s: str) -> int:
        ri = {
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1,
        }
        n = len(s)
        result=0
        i = 0 
        while i < n :

            if s[i] == 'I' and i + 1 < n:
                if s[i+1] == 'X':
                    result+=9
                    i+=2
                    continue
                if s[i+1] == 'V':
                    result+=4
                    i+=2
                    continue
            if s[i] == 'X' and i + 1 < n:
                if s[i+1] == 'L':
                    result+=40
                    i+=2
                    continue
                if s[i+1] == 'C':
                    result+=90
                    i+=2
                    continue
            if s[i] == 'C' and i + 1 < n:
                if s[i+1] == 'D':
                    result+=400
                    i+=2
                    continue
                if s[i+1] == 'M':
                    result+=900
                    i+=2
                    continue
            result += ri[s[i]]
            i+=1

        return result
            
          




        