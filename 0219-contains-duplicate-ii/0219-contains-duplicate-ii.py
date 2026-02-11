class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_i = {}

        for i in range(len(nums)):
            if nums[i] in num_to_i:
                j = num_to_i[nums[i]]
                
                if i - j <= k :
                    return True

            num_to_i[nums[i]] = i 

        return False