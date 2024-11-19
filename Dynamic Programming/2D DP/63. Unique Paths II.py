def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def solve(i,j,m,n,arr):
        if i==m-1 and j==n-1:
            return 1
        if i>=m or j>=n:
            return 0
        if arr[i][j]==1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        right=solve(i,j+1,m,n,arr)
        left=solve(i+1,j,m,n,arr)
        dp[i][j]=left+right
        return dp[i][j]
    dp=[]
    m=len(obstacleGrid)
    n=len(obstacleGrid[0])
    for i in range(m):
        dp.append([-1]*n)
    if obstacleGrid[m-1][n-1]==1:
        return 0
    return solve(0,0,m,n,obstacleGrid)