arr=[1,2,3,2,2]
hashmap={}
left=0
max1=0
right=0
n=len(arr)
while right<n:
    if arr[right] in hashmap:
        hashmap[arr[right]]+=1
        right=right+1
    else:
        hashmap[arr[right]]=1
        right=right+1
# print(hashmap)
# print(len(hashmap))
    while len(hashmap)>2 and left<n:
        # max1=max(max1,right-left)
        hashmap[arr[left]]-=1
        print(hashmap)
        if hashmap[arr[left]]==0:
            del hashmap[arr[left]]
        print(len(hashmap))
        left=left+1
    max1=max(max1,right-left)
print(max1)
    

    

