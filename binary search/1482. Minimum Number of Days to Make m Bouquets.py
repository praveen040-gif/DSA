def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    def ispossible(m,k,arr,day):
        took=0
        for i in range(len(arr)):
            if day>=arr[i]:
                took+=1
            else:
                took=0
            if took==k:
                m-=1
                took=0
            if m==0:
                return True
        return False
    if m*k > len(bloomDay):
        return -1
    low=1
    high=max(bloomDay)
    while low<=high:
        mid=(low+high)//2
        if ispossible(m,k,bloomDay,mid)==True:
            high=mid-1
        else:
            low=mid+1
    return low