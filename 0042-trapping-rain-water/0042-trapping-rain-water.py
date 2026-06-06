class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n 
        max_right = [0] * n 
        
        l_wal= r_wal =0
        for i in range(n):
            j = -i-1
            
            max_left[i] = l_wal
            max_right[j] = r_wal

            l_wal = max(l_wal ,height[i])
            r_wal = max(r_wal ,height[j])


        water=0

        for i in range(n):
            p_trap = min(max_right[i],max_left[i])

            water += max(p_trap - height[i] , 0 )

        return water            

            