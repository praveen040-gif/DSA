def minWindow(self, s: str, t: str) -> str:
    n=len(s)
    m=len(t)
    if m>n:
        return ""
    right=0
    left=0
    i=0
    hashmap1={}
    ans=""
    min1=float('inf')
    while i<m:
        if t[i] in hashmap1:
            hashmap1[t[i]]+=1
        else:
            hashmap1[t[i]]=1
        i+=1
    count=len(hashmap1)
    while right<n:
        if s[right] in hashmap1:
                hashmap1[s[right]]-=1
                if hashmap1[s[right]]==0:
                    count-=1
        while count==0:
            if right-left+1<min1:
                ans=s[left:right+1]
                min1=right-left+1
            if s[left] in hashmap1:
                hashmap1[s[left]]+=1
                if hashmap1[s[left]]==1:
                    count+=1
            left=left+1
        right+=1
    return ans