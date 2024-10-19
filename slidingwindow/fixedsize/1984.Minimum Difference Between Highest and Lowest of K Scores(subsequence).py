#technique---->sort the array 
def minimumDifference(nums,k):
    nums.sort()
    right=0
    n=len(nums)
    min1=float("inf")
    while right<n:
        l=nums[right:right+k]
        if len(l)==k:
            min1=min(min1,abs(l[0]-l[-1]))
        right=right+1
    return min1
nums=list(map(int,input().split()))
k=int(input())
ans=minimumDifference(nums,k)
print(ans)