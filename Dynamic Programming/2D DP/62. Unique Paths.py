def uniquePaths(self, m: int, n: int) -> int:
    def path(i,j):            
        if i==m-1 and j==n-1:
            return 1
        if j>=n or i>=m:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        left=path(i,j+1)
        right=path(i+1,j)
        # print(left,right)
        dp[i][j]=left+right
        return dp[i][j]
    dp=[]
    for i in range(m+1):
        dp.append([-1]*n)
    count=0
    k=path(0,0)
    # print(dp)
    return k