def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    def atmost(nums,k):
        n=len(nums)
        right=0
        left=0
        ans=0
        hashmap={}
        while right<n:
            if nums[right] in hashmap:
                hashmap[nums[right]]+=1
            else:
                hashmap[nums[right]]=1
            right=right+1
            while len(hashmap)>k:
                hashmap[nums[left]]-=1
                if hashmap[nums[left]]==0:
                    del hashmap[nums[left]]
                left=left+1
            ans=ans+(right-left)
            print(ans)
        return ans
    res=atmost(nums,k)-atmost(nums,k-1)
    return res