class Solution:
    def canJump(self, nums: List[int]) -> bool:


        """
        biggest jump can reach for what?

        """
        
        max_reach =nums[0]

        for i in range(1, len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach , i + nums[i])

        return True 