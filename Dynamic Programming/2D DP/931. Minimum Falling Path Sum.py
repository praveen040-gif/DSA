class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def solve(i,j,n,dp):
            if i>=n or j>=n or j<0:
                return float('inf')
            if i==n-1:
                return matrix[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            ldiagonal=matrix[i][j]+solve(i+1,j-1,n,dp)
            rdiagonal=matrix[i][j]+solve(i+1,j+1,n,dp)
            down=matrix[i][j]+solve(i+1,j,n,dp)
            dp[i][j]=min(ldiagonal,rdiagonal,down)
            return dp[i][j]
        n=len(matrix)
        min1=float('inf')
        dp=[]
        for i in range(n):
            dp.append([-1]*n)
        for k in range(n):
            ans=solve(0,k,n,dp)
            min1=min(min1,ans)
        return min1



        