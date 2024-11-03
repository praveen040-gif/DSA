def permutation(l,arr):
    if len(l)==len(arr):
        print(l)
        ans.append(l[:])
        return
    for i in range(len(arr)):
        if arr[i] not in l:
            l.append(arr[i])
            permutation(l,arr)
            l.pop()
arr=list(map(int,input().split()))
l=[]
ans=[]
permutation(l,arr)
print(ans)
print(len(ans))

