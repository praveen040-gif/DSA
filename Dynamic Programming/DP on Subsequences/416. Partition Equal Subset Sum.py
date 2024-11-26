class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def solve(i,target,sum1,dp):
            if sum1>target:
                return False
            elif sum1==target:
                return True
            if i>=len(nums):
                return False
            if dp[i][sum1]!=-1:
                return dp[i][sum1]
            sum1=sum1+nums[i]
            pick=solve(i+1,target,sum1,dp)
            sum1-=nums[i]
            notpick=solve(i+1,target,sum1,dp)
            dp[i][sum1]=pick or notpick
            return dp[i][sum1]
        ans=sum(nums)
        if ans%2==1:
            return False
        n=len(nums)
        target=ans//2
        print(target)
        dp=[]
        for i in range(n):
            dp.append([-1]*(target+1))
        return solve(0,target,0,dp)
        