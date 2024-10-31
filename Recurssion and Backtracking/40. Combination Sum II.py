def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def comb(ind,l,sum1,target,arr):
        if sum1==target:
            ans.append(l[:])
            return 
        elif sum1>target:
            return
        for i in range(ind,len(arr)):
            if i!=ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            l.append(arr[i])
            sum1+=arr[i]
            comb(i+1,l,sum1,target,arr)
            sum1-=arr[i]
            l.pop()
        return
    candidates.sort()
    ans=[]
    l=[]
    comb(0,l,0,target,candidates)
    return ans