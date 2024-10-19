def countGoodSubstrings(s):
    right=0
    l=[]
    n=len(s)
    count=0
    while right<n:
        if s[right] not in l:
            l.append(s[right])
            right=right+1
        else:
            l.pop(0)
        if len(l)==3:
            count=count+1
            l.pop(0)
    return count
s=input()
ans=countGoodSubstrings(s)
print(ans)