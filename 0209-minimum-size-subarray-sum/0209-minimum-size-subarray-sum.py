class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minimum = float('inf')
        l, r =0 ,0
        sum = 0

        while r < len(nums) :
            sum += nums[r]

            while sum >= target :
                minimum = min(minimum , r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1

        return 0  if minimum == float("inf") else minimum