def arrayPairSum(nums):
    nums.sort()
    n=len(nums)
    right=0
    ans=[]
    while right<n:
        l=nums[right:right+2]
        ans.append(min(l))
        right=right+2
    return sum(ans)
nums=list(map(int,input().split()))
ans=arrayPairSum(nums)
print(ans)