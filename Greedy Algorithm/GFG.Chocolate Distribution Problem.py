def findMinDiff(self, arr,M):

    arr.sort()
    i=0 
    j=M-1
    ans=float('inf')
    while j<len(arr):
        diff=arr[j]-arr[i]
        ans=min(ans,diff)
        i=i+1
        j+=1
    return ans