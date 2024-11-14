def maximumPoints(self, arr, n):
    #memoization
    def allpossible(ind,last):
        if dp[ind][last]!=-1:
            return dp[ind][last]
        if ind==0:
            max1=0
            for i in range(3):
                if i!=last:
                    max1=max(arr[0][i],max1)
            dp[ind][last] = max1
            return dp[ind][last]
        max1=0
        for i in range(3):
            if i!=last:
                ans=arr[ind][i]+allpossible(ind-1,i)
                max1=max(max1,ans)
        dp[ind][last] = max1
        return dp[ind][last]
    #Tabulation
    dp=[]
    for i in range(n):
        dp.append([-1]*(4))
    dp[0][0] = max(arr[0][1], arr[0][2])
    dp[0][1] = max(arr[0][0], arr[0][2])
    dp[0][2] = max(arr[0][0], arr[0][1])
    dp[0][3] = max(arr[0][0], max(arr[0][1], arr[0][2]))
    for i in range(1,n):
        for last in range(4):
            dp[i][last]=0
            for j in range(3):
                if j!=last:
                    ans=arr[i][j]+dp[i-1][j]
                    dp[i][last]=max(ans,dp[i][last])
    return dp[n-1][3]
    # res=allpossible(n-1,3)
    # return res