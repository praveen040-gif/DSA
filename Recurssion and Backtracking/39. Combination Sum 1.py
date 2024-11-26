class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(i,sum1,l,arr,target):
            if i==len(arr):
                if sum1==target:
                    ans.append(l[:])
                return
            else:
                if sum1==target:
                    ans.append(l[:])
                    return
                elif sum1>target:
                    return
            l.append(arr[i])
            sum1+=arr[i]
            comb(i,sum1,l,arr,target)
            l.pop()
            sum1-=arr[i]
            comb(i+1,sum1,l,arr,target)
        ans=[]
        l=[]
        comb(0,0,l,candidates,target)
        return ans
        