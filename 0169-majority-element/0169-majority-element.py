class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] +=1 
        
        for n , f in freq.items():
            if f >= len(nums)/2:
                return n 

        return -1
