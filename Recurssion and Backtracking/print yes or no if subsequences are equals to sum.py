def comb(i,sum1,l,arr,target):
    if i==len(arr):
        if sum1==target:
            print(l)
            return True
        else:
            return False
    l.append(arr[i])
    sum1+=arr[i]
    if comb(i+1,sum1,l,arr,target)==True:
        return True
    l.pop()
    sum1-=arr[i]
    if comb(i+1,sum1,l,arr,target)==True:
        return True
arr=list(map(int,input().split()))
target=int(input())
l=[]
ans=comb(0,0,l,arr,target)
if ans==True:
    print("Yes")
else:
    print("No")