def comb(i,l,arr):
    if i>=len(arr):
        ans.append(l[:])
        return
    l.append(arr[i])
    comb(i+2,l,arr)
    l.pop()
    comb(i+1,l,arr)
arr=list(map(int,input().split()))
ans=[]
l=[]
comb(0,l,arr)
print(ans)

    