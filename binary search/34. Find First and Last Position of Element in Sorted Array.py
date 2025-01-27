# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
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