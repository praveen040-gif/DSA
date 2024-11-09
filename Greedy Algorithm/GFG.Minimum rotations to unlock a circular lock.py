def rotationCount(self, R, D):
    sum1=0
    while R!=0:
        ans1=R%10
        ans2=D%10
        sum1=sum1+min(abs(ans1-ans2),10-abs(ans1-ans2))
        R=R//10
        D=D//10
    return sum1