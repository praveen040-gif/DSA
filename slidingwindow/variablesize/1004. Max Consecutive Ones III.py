# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def ispossible(limit):
            right=0
            n=len(nums)
            left=0
            ones=0
            while right<n:
                if nums[right]==1:
                    ones+=1
                if right-left+1==limit:
                    if ones+k>=right-left+1:
                        return True
                    if nums[left]==1:
                        ones-=1
                    left+=1
                right+=1
            return False
        low=1
        high=len(nums)
        while low<=high:
            mid=(low+high)//2
            if ispossible(mid):
                low=mid+1
            else:
                high=mid-1
        return high
        