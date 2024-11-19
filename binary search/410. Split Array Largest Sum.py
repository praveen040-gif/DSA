def splitArray(self, nums: List[int], k: int) -> int:
    def ispossible(limit,k):
        sum1=0
        # print(limit)
        i=0
        while i<len(nums):
            sum1=sum1+nums[i]
            if sum1>limit:
                sum1=0
                k-=1
            else:
                i+=1
            if k<0:
                return False
        return True
    low=0
    high=sum(nums)
    while low<=high:
        mid=(low+high)//2
        if ispossible(mid,k-1):
            high=mid-1
        else:
            low=mid+1
    return low