# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        s=set()
        l=[]
        while i<j:
            k=i+1
            j=n-1
            while k<j:
                m=k+1
                j=n-1
                while m<j:
                    sum1=nums[i]+nums[k]+nums[m]+nums[j]
                    if sum1==target:
                        s.add((nums[i],nums[k],nums[m],nums[j]))
                        m+=1
                        j-=1
                    elif sum1<target:
                        m+=1
                    else:
                        j-=1
                k+=1
            i+=1
        l1=[]
        for i in s:
            l1.append(list(i))
        print(l1)

        return l1

        