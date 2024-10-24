arr=list(map(int,input().split()))
k=int(input())
i=0
c=0
while i<len(arr):
    if arr[i]==k:
        c=1
        break
    else:
        i=i+1
if c==1:
    print(i)
else:
    print(-1)