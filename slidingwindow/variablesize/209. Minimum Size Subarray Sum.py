def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    n=len(nums)
    if target>sum(nums):return 0
    right=0
    left=0
    sum1=0
    min1=float('inf')
    while right<n:
        sum1=sum1+nums[right]
        while sum1>=target and left<n:
            min1=min(min1,right-left+1)
            sum1=sum1-nums[left]
            left=left+1
        # min1=min(min1,right-left)
        right=right+1
    return min1