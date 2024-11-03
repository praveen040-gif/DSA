def merge(low,mid,high,arr):
    left=low
    right=mid+1
    temp=[]
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
def mergesort(low,high,arr):
    if low<high:
        mid=(low+high)//2
        mergesort(low,mid,arr)
        mergesort(mid+1,high,arr)
        merge(low,mid,high,arr)
arr=list(map(int,input().split()))
mergesort(0,len(arr)-1,arr)
print(arr)