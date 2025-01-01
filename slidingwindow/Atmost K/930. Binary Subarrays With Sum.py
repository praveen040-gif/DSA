# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# Example 2:

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(k):
            right=0
            left=0
            ans=0
            n=len(nums)
            sum1=0
            while right<n:
                sum1=sum1+nums[right]
                while sum1>k and left<n:
                    sum1-=nums[left]
                    left+=1
                ans+=(right-left+1)
                right+=1
            return ans
        if goal==0:
            return atmost(goal)
        return atmost(goal)-atmost(goal-1)
        