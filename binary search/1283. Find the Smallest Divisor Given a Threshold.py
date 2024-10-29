import math
def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    def ispossible(nums,threshold,k):
        for i in range(len(nums)):
            ans=math.ceil(nums[i]/k)
            threshold-=ans
        if threshold>=0:
            return True
        else:
            return False
    left=1
    right=max(nums)
    while left<=right:
        mid=(left+right)//2
        print(mid)
        if(ispossible(nums,threshold,mid)):
            right=mid-1
        else:
            left=mid+1
    return left