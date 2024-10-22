def lengthOfLongestSubstring(s):
    n=len(s)
    right=0
    l=[]
    max1=0
    while right<n:
        if s[right] not in l:
            l.append(s[right])
            right=right+1
        else:
            max1=max(max1,len(l))
            l.pop(0)
        max1=max(max1,len(l))
    return max1
s=input()
ans=lengthOfLongestSubstring(s)
print(ans)