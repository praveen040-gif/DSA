from os import *
from sys import *
from collections import *
from math import *
def solve(i,wt,n):
    if wt>weight:
        return 0
    if i>=n:
        return 0
    if dp[i][wt]!=-1:
        return dp[i][wt]
    take=0
    if wt+arr[i]<=weight:
        take=val[i]+solve(i+1,wt+arr[i],n)
    nottake=solve(i+1,wt,n)
    dp[i][wt]=max(take,nottake)
    return dp[i][wt]
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    val=list(map(int,input().split()))
    weight=int(input())
    dp=[]
    for i in range(n):
        dp.append([-1]*(weight+1))
    ans=solve(0,0,len(arr))
    print(ans)


