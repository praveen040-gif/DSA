def comb(i,sum1,l,arr,target):
    if i==len(arr):
        if sum1==target:
            print("hi")
        return
    else:
        if sum1==target:
            print(l)
            return
        elif sum1>target:
            return
    l.append(arr[i])
    sum1+=arr[i]
    comb(i,sum1,l,arr,target)
    l.pop()
    sum1-=arr[i]
    comb(i+1,sum1,l,arr,target)
arr=list(map(int,input().split()))
target=int(input())
l=[]
comb(0,0,l,arr,target)