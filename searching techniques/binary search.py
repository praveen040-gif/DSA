arr=list(map(int,input().split()))
k=int(input())
arr.sort()
low=0
high=len(arr)
c=0
while low<high:
    mid=(low+high)//2
    if arr[mid]==k:
        c=1
        break
    elif k>arr[mid]:
        low=mid+1
    else:
        high=mid
if c==1:
    print(mid)
else:
    print(-1)