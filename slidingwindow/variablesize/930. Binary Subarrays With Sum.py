def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def atmost(nums,goal):
        n=len(nums)
        right=0
        left=0
        sum1=0
        ans=0
        while right<n:
            sum1=sum1+nums[right]
            right=right+1
            while sum1>goal and left<n:
                sum1-=nums[left]
                left=left+1
            ans=ans+right-left
            print(right,left)
        return ans
    if goal==0:
        return atmost(nums,goal)
    return atmost(nums,goal)-atmost(nums,goal-1)