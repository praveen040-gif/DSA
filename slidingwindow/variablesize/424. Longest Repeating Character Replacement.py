def characterReplacement(self, s: str, k: int) -> int:
    hashmap={}
    n=len(s)
    right=0
    left=0
    maxfreq=0
    maxlen=0
    while right<n:
        if s[right] in hashmap:
            hashmap[s[right]]+=1
        else:
            hashmap[s[right]]=1
        maxfreq=max(maxfreq,hashmap[s[right]])
        right+=1
        if (right-left)-maxfreq>k:
            hashmap[s[left]]-=1
            maxfreq=max(hashmap.values())
            left+=1
        if (right-left)-maxfreq<=k:
            maxlen=max(maxlen,right-left)
    return maxlen