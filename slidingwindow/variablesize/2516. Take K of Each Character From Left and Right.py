def takeCharacters(self, s: str, k: int) -> int:
    if k==0:
        return 0
    hashmap={}
    n=len(s)
    for i in range(n):
        if s[i] in hashmap:
            hashmap[s[i]]+=1
        else:
            hashmap[s[i]]=1
    print(hashmap)
    if len(hashmap)<3:
        return -1
    if (hashmap['a']<k) or (hashmap['b']<k) or (hashmap['c']<k):
        return -1

    left=0
    right=0
    min1=float('inf')
    while right<n:
        hashmap[s[right]]-=1
        # print(hashmap)
        while min(hashmap.values())<k:
            hashmap[s[left]]+=1
            left+=1
        min1=min(min1,(n-(right-left+1)))
        right+=1
    return min1