class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res 
            else:
                minValue =  min(newInterval[0] ,  intervals[i][0] )
                maxValue =  max(newInterval[1] ,  intervals[i][1] )
                newInterval= [minValue, maxValue]

        res.append(newInterval)
        return res


