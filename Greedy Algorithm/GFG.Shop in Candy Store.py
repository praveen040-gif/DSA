def candyStore(self, candies,N,K):
    candies.sort()
    i=0
    sum1=0
    sum2=0
    while N>0:
        sum1=sum1+candies[i]
        sum2=sum2+candies[len(candies)-i-1]
        N=N-(K+1)
        i+=1
    return sum1,sum2