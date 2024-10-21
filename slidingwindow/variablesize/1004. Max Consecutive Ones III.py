def longestOnes( nums, k):
    n=len(nums)
    right=0
    left=0
    z=0
    max1=float('-inf')
    while right<n:
        if nums[right]==0:
            z=z+1
        while z>k:
            # max1=max(max1,right-left)
            print(max1)
            if nums[left]==0:
                z=z-1
            left=left+1
        right=right+1
        max1=max(max1,right-left)
    return max1
nums=list(map(int,input().split()))
k=int(input())
ans=longestOnes(nums,k)
print(ans)