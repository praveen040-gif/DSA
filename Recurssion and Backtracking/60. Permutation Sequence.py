def getPermutation(self, n: int, k: int) -> str:
    def factorial(n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    def permutation(n,l,k,s):
        if n<1:
            ans.append(s)
            return
        fact=factorial(n-1)
        k1=(k)//fact
        s=s+str(l[k1])
        k=k%fact
        l.pop(k1)
        permutation(n-1,l,k,s)

    l=[]
    for i in range(1,n+1):
        l.append(i)
    s=""
    ans=[]
    permutation(n,l,k-1,s)
    return ans[0]