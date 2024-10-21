def maxConsecutiveAnswers(answerKey,K):
    def maxt(answerKey, k):
        n=len(answerKey)
        right=0
        left=0
        f=0
        max1=float('-inf')
        while right<n:
            if answerKey[right]=='F':
                f=f+1
            while f>k:
                max1=max(max1,right-left)
                if answerKey[left]=='F':
                    f=f-1
                left=left+1
            max1=max(max1,right-left+1)
            right=right+1
        return max1
    def maxf(answerKey, k):
        n=len(answerKey)
        right=0
        left=0
        max1=float('-inf')
        f=0
        while right<n:
            if answerKey[right]=='T':
                f=f+1
            while f>k:
                max1=max(max1,right-left)
                if answerKey[left]=='T':
                    f=f-1
                left=left+1
            max1=max(max1,right-left+1)
            right=right+1
        return max1
    a=maxt(answerKey,k)
    b=maxf(answerKey,k)
    return max(a,b)
nums=list(map(int,input().split()))
k=int(input())
ans=maxConsecutiveAnswers(nums,k)
print(ans)