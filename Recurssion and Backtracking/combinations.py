def comb(l,i,arr):
    if i==len(arr):
        print(l)
        ans.append(l[:])
        return
    l.append(arr[i])
    comb(l,i+1,arr)
    l.pop()
    comb(l,i+1,arr)
arr=list(map(int,input().split()))
l=[]
ans=[]
comb(l,0,arr)
print(ans)