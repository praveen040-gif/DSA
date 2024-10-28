def isIsomorphic(self, s: str, t: str) -> bool:
    dici={}
    rev={}
    for i in range(len(s)):
        if s[i] not in dici and t[i] not in rev:
            dici[s[i]]=t[i]
            rev[t[i]]=s[i]
        elif s[i] in dici and dici[s[i]]!=t[i]:
            return False
        elif t[i] in rev and rev[t[i]]!=s[i]:
            return False
    return True