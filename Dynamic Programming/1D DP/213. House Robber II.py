def rob(self, nums: List[int]) -> int:
    def comb(i,arr):
        print(arr,i,len(arr))
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
    if len(nums)==1:
        return nums[0]
    dp=[-1]*(len(nums)+1)

    first=comb(0,nums[0:len(nums)-1])
    dp=[-1]*(len(nums)+1)
    last=comb(0,nums[1:len(nums)])
    return max(first,last)