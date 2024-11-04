def minPartition(self, n):
    arr=[1,2,5,10,20,50,100,200,500,2000]
    arr.sort(reverse=True)
    i=0
    l=[]
    while n>0:
        # ans=n//arr[i]
        # while ans!=0:
        #     l.append(arr[i])
        #     ans-=1
        # n=n%arr[i]
        #   i+=1
        if arr[i]>n:
            i+=1
        else:
            n=n-arr[i]
            l.append(arr[i])
    return l