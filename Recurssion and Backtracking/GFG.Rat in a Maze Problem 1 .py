def findPath(self, m: List[List[int]]) -> List[str]:
    def solve(i,j,m,v,l):
        if i==len(m)-1 and j==len(m)-1:
            ans.append("".join(l))
            return 
        #downward
        if(i+1<len(m) and m[i+1][j]==1 and v[i+1][j]==0):
            l.append('D')
            v[i][j]=1
            solve(i+1,j,m,v,l)
            v[i][j]=0
            l.pop()
        #left
        if(j-1>=0 and m[i][j-1]==1 and v[i][j-1]==0 ):
            l.append('L')
            v[i][j]=1
            solve(i,j-1,m,v,l)
            v[i][j]=0
            l.pop()
        #right
        if(j+1<len(m) and m[i][j+1]==1 and v[i][j+1]==0 ):
            l.append('R')
            v[i][j]=1
            solve(i,j+1,m,v,l)
            v[i][j]=0
            l.pop()
        #upward
        if(i-1>=0 and m[i-1][j]==1 and v[i-1][j]==0):
            l.append('U')
            v[i][j]=1
            solve(i-1,j,m,v,l)
            v[i][j]=0
            l.pop()
    ans=[]
    l=[]
    v=[]
    for i in range(len(m)):
        v.append([0]*len(m))
    if m[0][0]==1:
        solve(0,0,m,v,l)
        return ans
    else:
        return []