import math
def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def ispossible(nums,h,k):
        for i in range(len(nums)):
            ans=math.ceil(nums[i]/k)
            h=h-ans
        if h>=0:
            return True
        else:
            return False
    left=1
    right=max(piles)
    while left<=right:
        mid=(left+right)//2
        if(ispossible(piles,h,mid)):
            right=mid-1
        else:
            left=mid+1
    return left