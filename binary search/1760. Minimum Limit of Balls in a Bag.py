import math
def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    def ispossible(op,limit):
        for i in range(len(nums)):
            if nums[i]>limit:
                ans=math.ceil(nums[i]/limit)
                op=op-(ans-1)
                if op<0:
                    return False
        return True
    low=1
    high=max(nums)
    while low<=high:
        mid=(low+high)//2
        if ispossible(maxOperations,mid):
            high=mid-1
        else:
            low=mid+1
    return low