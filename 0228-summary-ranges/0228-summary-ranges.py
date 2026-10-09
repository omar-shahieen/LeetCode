class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        if len(nums) == 1 :
            return [str(nums[0])]
        # array is sorted , so i do not need to sort 
        a = b = 0 
        res = [ ]
        n = len(nums)
        # Loop over the nums 
        for i in range(n-1):
            if  nums[b+1] - nums[b] == 1:
                b += 1
            else: 
                interval = f"{nums[a]}" if a == b else f"{nums[a]}->{nums[b]}"
                res.append(interval)
                b += 1
                a = b 
        
        interval = f"{nums[a]}" if a == b else f"{nums[a]}->{nums[b]}"
        res.append(interval)

        return res 
    
        