def searchRange(self, nums: List[int], target: int) -> List[int]:
    def leftmost(nums,k):
        n=len(nums)-1
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            if k <= nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return left
    def rightmost(nums,k):
        n=len(nums)-1
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            if k >= nums[mid]:
                left=mid+1
            else:
                right=mid-1
        return right
    if target not in nums:
        return [-1,-1]
    return [leftmost(nums,target),rightmost(nums,target)]