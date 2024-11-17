def wordPattern(self, pattern: str, s: str) -> bool:
    s=s.split()
    if len(pattern)!=len(s):
        return False
    d1=[]
    d2=[]
    for i in range(len(s)):
        d1.append(pattern.index(pattern[i]))
        d2.append(s.index(s[i]))
    print(d1,d2)
    if d1==d2:
        return True
    return False