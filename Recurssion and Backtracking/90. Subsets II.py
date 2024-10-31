def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def comb(ind,l,arr):
        ans.append((l[:]))
        for i in range(ind,len(arr)):
            if i!=ind and arr[i]==arr[i-1]:
                continue
            l.append(arr[i])
            comb(i+1,l,arr)
            l.pop()
        # return
    nums.sort()
    l=[]
    ans=[]
    comb(0,l,nums)
    return ans