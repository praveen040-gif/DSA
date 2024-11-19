def qpivot(low,high,arr):
    pivot=low
    i=low
    j=high-1
    while i<j:
        while arr[i]<=arr[pivot] and i<high-1:
            i+=1
        while arr[j]>arr[pivot] and j>=low:
            j-=1
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[j]
    arr[j]=arr[pivot]
    arr[pivot]=temp
    return j
def qsort(low,high,arr):
    if low<high:
        pivot=qpivot(low,high,arr)
        qsort(low,pivot-1,arr)
        qsort(pivot+1,high,arr)
arr=list(map(int,input().split()))
qsort(0,len(arr),arr)
print(arr)