def comb(ind,l,arr):
    # if ind==len(arr):
    print(l)
        # return 
    for i in range(ind,len(arr)):
        if i!=ind and arr[i]==arr[i-1]:
            continue
        l.append(arr[i])
        comb(i+1,l,arr)
        l.pop()
    return
arr=list(map(int,input().split()))
l=[]
# ans=[]
comb(0,l,arr)
# print(ans)
    