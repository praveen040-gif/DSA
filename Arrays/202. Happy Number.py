def isHappy(self, n):
    l=[]
    sum1=0
    while n not in l:
        l.append(n)
        k=n
        while k!=0:
            rem=k%10
            sum1=sum1+(rem*rem)
            k=k//10
        if sum1==1:
            return True
        if k==0:
            n=sum1
            sum1=0
        print(l)
    return False