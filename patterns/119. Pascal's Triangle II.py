def getRow(self, rowIndex: int) -> List[int]:
    l=[] 
    ans=1
    num=1
    den=1
    l.append(ans)
    for i in range(rowIndex):
        num=num*(rowIndex-i)
        den=den*(i+1)
        ans=num//den
        l.append(ans)
    return l