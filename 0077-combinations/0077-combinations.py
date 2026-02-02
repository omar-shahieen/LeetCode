class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        """
        [1 , 2 , 3 ,4] 

        [1 , 2]
        [1,3]
        [1,4]
        [2,3]
        [3,4]
        []
        """

        res = [ ]
        comb = []

        def backtrack(start):
            if len(comb) + (n - start + 1) < k :
                return


            if len(comb) == k :
                res.append(comb[:])
                return


            for i in range(start,n + 1):
                comb.append(i)
                backtrack(i +1)
                comb.pop()

        backtrack(1)
        return res 