n=int(input())
s=""
while n!=0:
    ans=n%2
    s=s+str(ans)
    n=n//2
print(s[::-1])
