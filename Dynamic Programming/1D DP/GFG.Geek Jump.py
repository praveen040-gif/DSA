def minimumEnergy(self, height, n):
    #memoization
    def allpossible(ind,dp):
        right=float('inf')
        if ind==n-1:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        left=allpossible(ind+1,dp)+abs(height[ind]-height[ind+1])
        if ind<n-2:
            right=allpossible(ind+2,dp)+abs(height[ind]-height[ind+2])
        dp[ind]=min(left,right)
        return dp[ind]
    #Tablulation
    dp=[-1]*(n+1)
    dp[0]=0
    right=float('inf')
    for i in range(1,n):
        left=dp[i-1]+abs(height[i]-height[i-1])
        if i>1:
            right=dp[i-2]+abs(height[i]-height[i-2])
        dp[i]=min(left,right)
    return dp[n-1]