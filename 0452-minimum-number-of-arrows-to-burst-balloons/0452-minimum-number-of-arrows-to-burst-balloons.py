class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        

        arrows = 0 
        
        last_brust = float("-inf")

        for start , end in points:
            if start > last_brust:
                last_brust = end
                arrows += 1


        return arrows 
        