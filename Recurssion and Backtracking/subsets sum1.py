def subsetSums(self, arr, n):
    def comb(i,sum1,arr):
        if i==len(arr):
            ans.append(sum1)
            return
        sum1+=arr[i]
        comb(i+1,sum1,arr)
        sum1-=arr[i]
        comb(i+1,sum1,arr)
    ans=[]
    comb(0,0,arr)
    return ans