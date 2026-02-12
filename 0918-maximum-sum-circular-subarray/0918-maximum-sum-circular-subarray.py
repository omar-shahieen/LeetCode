class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        # min sub array 
        min_sum = nums[0]
        cur_min = nums[0]
        for num in nums[1:]:
            cur_min = min(cur_min + num , num)
            min_sum = min(min_sum , cur_min)

        # max sub array 
        max_sum = nums[0]
        cur_max = nums[0]
        for num in nums[1:]:
            cur_max = max(cur_max + num , num)
            max_sum = max(max_sum , cur_max)

        if max_sum < 0 :
            return max_sum
        return max(total - min_sum , max_sum)
