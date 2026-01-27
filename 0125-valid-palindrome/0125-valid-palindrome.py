class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []

        for c in s: 
            if 'a' <= c <= 'z' or 'A' <= c <= 'Z' or  '0' <= c <= "9":
                str.append(c.lower())

        
        i , j = 0 , len(str) - 1 

        while i < j : 
            if str[i] != str[j]:
                return False
            
            j -= 1
            i += 1 

        return True