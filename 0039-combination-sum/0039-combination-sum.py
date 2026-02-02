class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        idx -> 0 to n-1
        path = []
        res = [ [] ]
        pathSum : int

        if pathSum == target 
            add path to res 
        
        start from 0 to n :
            choose the number 

            rec(idx  , pathSum + nums[i])
            rec(idx + 1 , pathSum + nums[i])
            pop the number from the path
            
        """

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
