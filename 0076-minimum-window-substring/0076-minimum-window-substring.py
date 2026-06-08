class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map =Counter(t)
        s_map = defaultdict(int)
        

        required = len(t_map)
        formed = 0 

        min_window = ""
        l = 0     
        for r in range(len(s)):
            c = s[r]
            s_map[c] +=1

            if c in t_map and t_map[c] == s_map[c]:
                formed +=1


            while formed == required:  
                window = s[l:r+1]

                if not min_window or len(window) < len(min_window):
                    min_window = window 
                

                s_map[s[l]] -=1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    formed -=1

                l += 1

                
        return min_window

        