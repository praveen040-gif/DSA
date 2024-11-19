def minPathSum(self, grid: List[List[int]]) -> int:
    def solve(i,j,m,n):
        if i==m-1 and j==n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        right=grid[i][j]+solve(i,j+1,m,n)
        down=grid[i][j]+solve(i+1,j,m,n)
        dp[i][j]=min(right,down)
        return dp[i][j]
    m=len(grid)
    n=len(grid[0])
    dp=[]
    for i in range(m):
        dp.append([-1]*n)
    return solve(0,0,m,n)