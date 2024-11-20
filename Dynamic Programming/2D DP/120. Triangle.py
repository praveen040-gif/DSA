def minimumTotal(self, triangle: List[List[int]]) -> int:
    def solve(i,j,n):
        if i==n-1:
            return triangle[i][j]
        if i>=n:
            return float('inf')
        if dp[i][j]!=-1:
            return dp[i][j]
        down=triangle[i][j]+solve(i+1,j,n)
        diagonal=triangle[i][j]+solve(i+1,j+1,n)
        dp[i][j]= min(down,diagonal)
        return dp[i][j]
    n=len(triangle)
    dp=[]
    for i in range(n):
        dp.append([-1]*(i+1))
    return solve(0,0,n)