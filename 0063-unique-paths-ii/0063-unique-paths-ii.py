class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [  [0]*m for i in range(n)]
        if obstacleGrid[0][0] != 1 :
            dp[0][0] = 1
        for i in range(n):
            for j in range(m): 
                if obstacleGrid[i][j] != 1 :
                    if i - 1 >=0 :
                        dp[i][j] += dp[i-1][j]
                    if j - 1 >=0 :
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]
        