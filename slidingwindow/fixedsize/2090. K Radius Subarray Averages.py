def getAverages(self, nums: List[int], k: int) -> List[int]:
    n=len(nums)
    left=0
    ans=[-1]*n
    k1=k*2+1
    if len(nums)<k1:
        return [-1]*n
    val=sum(nums[0:k1])
    avg=val//k1
    ans[k]=avg
    right=k+1
    while right<n-k:
        if (right-k-1)>=0 and (right+k<n):
            val-=nums[right-k-1]
            val+=nums[right+k]
            avg=val//(k1)
            ans[right]=avg
        right+=1
    return ans