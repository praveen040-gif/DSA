# Given an integer array nums and an integer k, return the number of good subarrays of nums.

# A good array is an array where the number of different integers in that array is exactly k.

# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            right=0
            left=0
            n=len(nums)
            ans=0
            hashmap={}
            while right<n:
                if nums[right] in hashmap:
                    hashmap[nums[right]]+=1
                else:
                    hashmap[nums[right]]=1
                while len(hashmap)>k:
                    hashmap[nums[left]]-=1
                    if hashmap[nums[left]]==0:
                        del hashmap[nums[left]]
                    left+=1
                ans+=(right-left+1)
                right+=1
            return ans
        return atmost(k)-atmost(k-1)

        