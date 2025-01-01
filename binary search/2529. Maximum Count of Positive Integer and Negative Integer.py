# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

 

# Example 1:

# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:

# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:

# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def leftmost(k):
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if k<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            return low
        def rightmost(k):
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if k>=nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
            return high
        ans1=leftmost(0)
        print(ans1)
        ans2=len(nums)-rightmost(0)-1
        return max(ans1,ans2)
        
        