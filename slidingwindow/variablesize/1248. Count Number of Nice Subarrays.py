def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def atmost(nums,k):
        n=len(nums)
        right=0
        left=0
        odd=0
        ans=0
        while right<n:
            if nums[right]%2==1:
                odd=odd+1
            right=right+1
            while odd>k:
                if nums[left]%2==1:
                    odd-=1
                left=left+1
            ans=ans+(right-left)
        return ans
    res=atmost(nums,k)-atmost(nums,k-1)
    print(res)
    return res