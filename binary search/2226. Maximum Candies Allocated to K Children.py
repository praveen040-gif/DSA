def maximumCandies(self, candies: List[int], k: int) -> int:
    def ispossible(limit,k):
        for i in range(len(candies)):
            if candies[i]==limit:
                k=k-1
            if candies[i]>limit:
                ans=candies[i]//limit
                k=k-ans
            if k<=0:
                return True
        return False
    low=1
    high=max(candies)
    if sum(candies)<k:
        return 0
    while low<=high:
        mid=(low+high)//2
        if ispossible(mid,k):
            low=mid+1
        else:
            high=mid-1
    return high