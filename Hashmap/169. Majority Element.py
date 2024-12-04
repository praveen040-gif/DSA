# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
def majorityElement(self, nums: List[int]) -> int:
    n=len(nums)
    hashmap={}
    for i in range(n):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
        else:
            hashmap[nums[i]]=1
    for i in hashmap:
        if hashmap[i]>n//2:
            return i