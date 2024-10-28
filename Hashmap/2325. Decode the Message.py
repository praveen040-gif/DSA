def decodeMessage(self, key: str, message: str) -> str:
    s="abcdefghijklmnopqrstuvwxyz"
    s1={}
    i=0
    ans=""
    for k in range(len(key)):
        if key[k]!=" ":
            if key[k] not in s1:
                s1[key[k]]=i
                i+=1
    for m in message:
        if m==" ":
            ans=ans+m
        else:
            ans=ans+s[s1[m]]
    return ans