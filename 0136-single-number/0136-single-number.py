class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        unique=nums[0]
        for i in range(1,len(nums)) :
            unique^= nums[i]
        return unique

        