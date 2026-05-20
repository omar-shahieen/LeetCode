class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        [a,b,c]
        c =b and c!= a replace
        c = a = b  start +1 
        c != a c !=b and a= b  skip
        c != a c !=b and a != b skip


        """
        n = len(nums)
        if n== 2 :
            return 2 
        
        start = 1
        for i in range(2,n):
            if (nums[i] != nums[start] and nums[i] != nums[start -1 ]) or (nums[i] == nums[start] and nums[i] != nums[start -1 ]):
                start += 1
                nums[start ] = nums[i]

        return start+1