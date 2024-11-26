class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m=len(box)
        n=len(box[0])
        for i in range(m):
            if box[i][0]=='#':
                prev=0
            else:
                prev=1
            for j in range(1,n):
                # print(prev)
                if box[i][j]=='.' and box[i][j-1]=='#':
                    temp=box[i][j]
                    box[i][j]=box[i][prev]
                    box[i][prev]=temp
                    prev+=1
                elif box[i][j]=='.' or box[i][j]=='*':
                    prev=j+1
        # return box
        res=[]
        for i in range(n):
            ans=[]
            for j in range(m-1,-1,-1):
                ans.append(box[j][i])
            res.append(ans)
        return res
            

        