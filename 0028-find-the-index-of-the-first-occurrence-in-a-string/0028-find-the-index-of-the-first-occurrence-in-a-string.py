class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m > n :
            return -1

        for i in range(n):
            k =i 
            for j in range(m):
                
                if k == n or haystack[k] != needle[j]:
                    break
                if j == m-1 and haystack[k] == needle[j]:
                    return i
                k = k+1

        return -1


            
            