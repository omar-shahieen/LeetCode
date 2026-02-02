class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        path = []
        res = [] 
        n = len(candidates)
        
        def backtrack(idx , pathSum):
            if pathSum == target :
                res.append(path[:])
                return 
            if idx == n or  pathSum > target : 
                return

            # take the number with reuse
            path.append(candidates[idx])
            backtrack(idx , pathSum + candidates[idx])
            path.pop()

            # skip the number
            backtrack(idx + 1, pathSum )


        backtrack(0 , 0 )
        return res
