def numOfSubarrays(arr, k, threshold):
    n=len(arr)
    right=0
    left=0
    sum1=0
    count=0
    while right<n:
        sum1=sum1+arr[right]
        if right-left+1==k:
            ans=sum1//k
            if ans>=threshold:
                count=count+1
            sum1=sum1-arr[left]
            left=left+1
            right=right+1
        else:
            right+=1
    return count
nums=list(map(int,input().split()))
k=int(input())
threshold=int(input())
ans=numOfSubarrays(nums,k,threshold)
print(ans)