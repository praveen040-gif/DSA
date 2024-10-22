def findAnagrams(s, p):
    hashmap1={}
    k=len(p)
    for i in range(k):
        if p[i] in hashmap1:
            hashmap1[p[i]]+=1
        else:
            hashmap1[p[i]]=1
    hashmap2={}
    n=len(s)
    right=0
    left=0
    l=[]
    while right<n:
        if s[right] in hashmap2:
            hashmap2[s[right]]+=1
        else:
            hashmap2[s[right]]=1
        if right-left+1==k:
            print(hashmap1,hashmap2)
            if hashmap1==hashmap2:
                l.append(left)
            hashmap2[s[left]]-=1
            if hashmap2[s[left]]==0:
                del hashmap2[s[left]]
            left=left+1
        right=right+1
    return l
