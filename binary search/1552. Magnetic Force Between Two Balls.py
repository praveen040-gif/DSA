def maxDistance(self, position: List[int], m: int) -> int:
    def ispossible(n,limit,k):
        i=1
        prev=position[0]
        while i<n:
            val=position[i]
            if (val-prev)>=limit:
                k-=1
                prev=val
                if k<=0:
                    return True
            i+=1
        return False
    low=0
    high=max(position)
    position.sort()
    while low<=high:
        mid=(low+high)//2
        if ispossible(len(position),mid,m-1):
            low=mid+1
        else:
            high=mid-1
    return high