import math
def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    def ispossible(limit):
        sum1=0
        for i in range(len(quantities)):
            sum1=sum1+math.ceil(quantities[i]/limit)
        if sum1<=n:
            return True
        return False
    low=1
    high=max(quantities)
    while low<=high:
        mid=(low+high)//2
        if ispossible(mid):
            high=mid-1
        else:
            low=mid+1
    return low