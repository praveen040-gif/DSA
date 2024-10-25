def maximumCount(self, nums: List[int]) -> int:
    n=len(nums)
    def leftmost(nums,k):
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if k<=nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return left
    return max(leftmost(nums,0),n-leftmost(nums,1))