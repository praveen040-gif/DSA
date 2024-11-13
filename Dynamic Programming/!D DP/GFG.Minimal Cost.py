def minimizeCost(self, k, arr):
    #Memoization
    def allpossible(ind,min1,dp):
        if ind==0:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        for i in range(1,k+1):
            if ind-i<0:
                break
            ans=allpossible(ind-i,min1,dp)+abs(arr[ind]-arr[ind-i])
            min1=min(ans,min1)
        dp[ind]=min1
        return dp[ind]
    #Tabulation
    dp=[-1]*(len(arr)+1)
    dp[0]=0
    for i in range(1,len(arr)):
        min1=float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                ans=dp[i-j]+abs(arr[i]-arr[i-j])
            min1=min(ans,min1)
            dp[i]=min1
    return dp[len(arr)-1]