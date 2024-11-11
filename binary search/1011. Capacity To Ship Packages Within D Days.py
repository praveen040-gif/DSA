def shipWithinDays(self, weights: List[int], days: int) -> int:
    def ispossible(arr,days,capacity):
        sum1=0
        i=0
        while i<len(arr):
            sum1=sum1+arr[i]
            if arr[i]>capacity:
                return False
            if sum1<=capacity:
                i+=1
            else:
                days-=1
                sum1=0
        if days>0:
            return True
        else:
            return False
    low=0
    high=sum(weights)
    while low<=high:
        mid=(low+high)//2
        if ispossible(weights,days,mid):
            high=mid-1
        else:
            low=mid+1
    return low