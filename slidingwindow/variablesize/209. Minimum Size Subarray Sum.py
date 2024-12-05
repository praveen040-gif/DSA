# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        n=len(nums)
        right=0
        sum1=0
        min1=float('inf')
        while right<n:
            sum1+=nums[right]
            while sum1>=target:
                min1=min(min1,right-left+1)
                sum1-=nums[left]
                left+=1
            right+=1
        if min1!=float('inf'):
            return min1
        return 0