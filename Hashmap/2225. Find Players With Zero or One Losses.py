def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    hashmap={}
    ans1=[]
    ans2=[]
    for x,y in matches:
        if y in hashmap:
            hashmap[y]+=1
        else:
            hashmap[y]=1
    for x,y in matches:
        if x not in hashmap:
            ans1.append(x)
            hashmap[x]=2
        if hashmap[y]==1:
            ans2.append(y)
    ans1.sort()
    ans2.sort()
    return [ans1,ans2]