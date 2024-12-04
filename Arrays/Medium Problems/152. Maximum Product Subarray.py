# return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        pref=1
        suff=1
        max1=float('-inf')
        for i in range(n):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[n-1-i]
            ans=max(pref,suff)
            max1=max(max1,ans)
        return max1
        