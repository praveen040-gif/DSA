class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])
        l=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    l.append([i,j])
        for x,y in l:
            for i in range(m):
                matrix[x][i]=0
            for j in range(n):
                matrix[j][y]=0

        
        