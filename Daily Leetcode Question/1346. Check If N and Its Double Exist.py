class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n=len(arr)
        hashmap={}
        for i in range(n):
            if arr[i] in hashmap:
                hashmap[arr[i]]+=1
            else:
                hashmap[arr[i]]=1
        for i in range(n):
            ans=2*arr[i]
            if ans==0:
                if hashmap[ans]>1:
                    return True
            elif ans in hashmap:
                return True
        return False
        