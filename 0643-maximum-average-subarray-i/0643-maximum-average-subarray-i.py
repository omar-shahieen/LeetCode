class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        num_sum = sum(nums[0:k])
        max_avg = num_sum/k

        for i in range(k , len(nums)):
            num_sum -= nums[i-k]
            num_sum += nums[i] 
            avg_sum = num_sum/k 

            max_avg = max(avg_sum,max_avg)

        return max_avg
