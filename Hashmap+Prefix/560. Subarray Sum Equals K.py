# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        right=0
        hashmap=defaultdict(int)
        print(hashmap)
        hashmap[0]=1
        sum1=0
        ans=0
        while right<n:
            sum1+=nums[right]
            rem=sum1-k
            if rem in hashmap:
                ans+=hashmap[rem]
            hashmap[sum1]+=1
            right+=1
        return ans
        