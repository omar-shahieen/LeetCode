class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNums = nums[:]
        n= len(nums)
        for i in range(n):
            nums[(i+k)%n] = lastNums[i] 
