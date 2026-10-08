class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # sort the citations descending 

        citations.sort(reverse=True)
        # compare until positoin i > citation[i]
        i = 0 
        n = len(citations)
        while i < n and  (i + 1) <= citations[i]:
            i = i + 1
        
        return i 
