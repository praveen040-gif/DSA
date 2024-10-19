def minimumCost(cost):
    cost.sort()
    n=len(cost)
    ans=[]
    if n==2:
        return sum(cost)
    right=n-1
    c=0
    while right>=0:
        ans.append(cost[right])
        right=right-1
        c=c+1
        if c==2:
            right=right-1
            c=0
    return sum(ans)
nums=list(map(int,input().split()))
ans=minimumCost(nums)
print(ans)