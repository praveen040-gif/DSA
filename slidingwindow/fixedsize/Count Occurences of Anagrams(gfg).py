def search(self,pat, txt):
    n=len(txt)
    m=len(pat)
    i=0
    left=0
    right=0
    h1={}
    h2={}
    c=0
    while i<m:
        if pat[i] in h1:
            h1[pat[i]]+=1
        else:
            h1[pat[i]]=1
        i+=1
    while right<n:
        if txt[right] in h1:
            if txt[right] in h2:
                h2[txt[right]]+=1
            else:
                h2[txt[right]]=1
        right+=1
        if right-left==m and left<n:
            if h1==h2:
                c=c+1
            if txt[left] in h2:
                h2[txt[left]]-=1
                if h2[txt[left]]==0:
                    del h2[txt[left]]
            left+=1
    return c