def partition(self, s: str) -> List[List[str]]:
    def palindrome(i,index,s):
        k=s[index:i+1]
        return k==k[::-1]
    def solve(index,s):
        if index==len(s):
            ans.append(l[:])
            return
        for i in range(index,len(s)):
            if(palindrome(i,index,s)):
                l.append(s[index:i+1])
                solve(i+1,s)
                l.pop()
    l=[]
    ans=[]
    solve(0,s)
    return ans