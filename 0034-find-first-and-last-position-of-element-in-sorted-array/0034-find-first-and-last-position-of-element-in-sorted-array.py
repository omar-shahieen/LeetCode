class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l , r =  0 , len(nums) - 1 
        start , end  = -1 , -1 

        # search for start of range 
        while l <= r :
            m =  l + (r-l)//2 

            if nums[m] == target :
                start = m 
                r = m-1
            elif nums[m] > target : 
                r = m -1 
            else : 
                l = m + 1

        
        # search for end of range 
        l , r =  0 , len(nums) - 1 

        while l <= r :
            m =  l + (r-l)//2 

            if nums[m] == target :
                end = m 
                l = m+1
            elif nums[m] > target : 
                r = m -1 
            else : 
                l = m + 1





        return [start , end]