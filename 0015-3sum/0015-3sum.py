
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        
        results = []
        n= len(nums)
        i =0
        while i  < n-2:
            while i > 0 and i < n-2 and  nums[i] == nums[i-1]:
                i += 1
                continue

                
            target = - nums[i]
            j, k =  i+1 , n - 1
            
            
            while j < k: 
                curr_sum =  nums[j] + nums[k]
                if curr_sum == target:
                    results.append( [nums[i] , nums[j], nums[k]])
                    j +=1 
                    k -= 1
                    
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                        
                
                elif curr_sum > target :
                    k -= 1
                else :
                    j += 1
            i += 1
            

        return results
  
  
  