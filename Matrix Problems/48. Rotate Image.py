class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        l=[]
        for i in range(m):
            x=[]
            for j in range(m-1,-1,-1):
                x.append(matrix[j][i])
            l.append(x)
        for i in range(len(l)):
            for j in range(len(l[0])):
                matrix[i][j]=l[i][j]
        

        