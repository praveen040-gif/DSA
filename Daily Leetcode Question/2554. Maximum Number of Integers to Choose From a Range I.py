class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        c=0
        sum1=0
        banned=set(banned)
        for i in range(1,n+1):
            if i not in banned:
                sum1=sum1+i
                if sum1<=maxSum:
                    c+=1
                else:
                    return c
        return c
        