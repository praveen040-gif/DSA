class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def ispossible(limit):
            right=0
            left=0
            sum1=0
            n=len(nums)
            while right<n:
                sum1=sum1+nums[right]
                if right-left+1==limit:
                    ans=limit*nums[right]
                    res=ans-sum1
                    if res<=k:
                        return True
                    else:
                        sum1-=nums[left]
                        left+=1
                right+=1
            return False
        nums.sort()
        n=len(nums)
        low=1
        high=n
        while low<=high:
            mid=(low+high)//2
            if ispossible(mid):
                low=mid+1
            else:
                high=mid-1
        return high

        