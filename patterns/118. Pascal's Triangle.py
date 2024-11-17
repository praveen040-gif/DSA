def generate(self, numRows: int) -> List[List[int]]:
    def pascal(n):
        fin=1
        l=[]
        l.append(fin)
        num=1
        den=1
        for i in range(n):
            num=num*(n-i)
            den=den*(i+1)
            fin=num//den
            l.append(fin)
        return l
    res=[]
    for i in range(numRows):
        ans=pascal(i)
        res.append(ans)
    return res