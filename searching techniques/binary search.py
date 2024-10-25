arr=list(map(int,input().split()))
k=int(input())
arr.sort()
low=0
high=len(arr)-1
c=0
while low<=high:
    mid=(low+high)//2
    if arr[mid]==k:
        c=1
        break
    elif k>arr[mid]:
        low=mid+1
    else:
        high=mid-1
if c==1:
    print(mid)
else:
    print(-1)