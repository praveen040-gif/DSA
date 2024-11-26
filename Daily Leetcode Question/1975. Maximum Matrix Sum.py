class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min1=float('inf')
        total=0
        neg=0
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                total+=abs(matrix[i][j])
                if matrix[i][j]<0:
                    neg+=1
                min1=min(min1,abs(matrix[i][j]))
        if neg%2==1:
            total-=(2*min1)
        return total