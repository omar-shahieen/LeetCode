class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        minimum  = inf
        sum = nums[0] 
        l = 0  , r = 1 
        while r < n 
            sum = sum + right

            while sum >= target 
                minimum = min(minimum , r - l  + 1)
                sum -= left 
                l ++ 
            
            r ++
        """

        minimum = float('inf')
        l, r =0 ,1 
        sum = nums[0]

        if sum >= target :
            minimum = 1
        while r < len(nums) :
            sum += nums[r]

            while sum >= target :
                minimum = min(minimum , r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1

        return 0  if minimum == float("inf") else minimum