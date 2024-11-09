arr=[4,3,2,1]
l=[]
l=(arr[:])
l.sort()
print(l)
swap=0
print(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            swap+=1
    if arr==l:
        print(swap)
        break

