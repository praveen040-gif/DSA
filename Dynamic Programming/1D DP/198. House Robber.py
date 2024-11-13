def rob(self, nums:List[int]) -> int:
    #Memoization
    def comb(i,arr):
        if i==len(arr)-1:
            return arr[i]
        if i>=len(arr):
            return 0
        if dp[i]!=-1:
            return dp[i]
        pick=arr[i]+comb(i+2,arr)
        notpick=0+comb(i+1,arr)
        dp[i]=max(pick,notpick)
        return dp[i]
    #Tabulation
    dp=[-1]*len(nums)
    n=len(nums)
    dp[0]=nums[0]
    for i in range(1,n):
        if i-2>=0:
            pick=nums[i]+dp[i-2]
        else:
            pick=nums[i]+0
        if i-1>=0:
            notpick=0+dp[i-1]
        else:
            pick=nums[i]+0
        dp[i]=max(pick,notpick)
    return dp[n-1]
    