class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        l=[]
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for i in range(top,bottom+1):
                l.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    l.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    l.append(matrix[i][left])
                left+=1
        return l

        