def maximumMeetings(self,start,end):
    l=[]
    for i in zip(start,end):
        l.append(list(i))
    l.sort(key=lambda x:x[1])
    prev=l[0][1]
    count=1
    for i in range(1,len(l)):
        if l[i][0]>prev:
            count+=1
            prev=l[i][1]
    return count