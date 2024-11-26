from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, target, arr):
    def solve(i,sum1,target,arr,dp):
        if sum1>target:
            return False
        elif sum1==target:
            return True
        if i>=len(arr):
            return False
        if dp[i][sum1]!=-1:
            return dp[i][sum1]
        a=False
        if arr[i]<=target:
            a=solve(i+1,sum1+arr[i],target,arr,dp)
        b=solve(i+1,sum1,target,arr,dp)
        if (a==True) or (b==True):
            dp[i][sum1]=True
        else:
            dp[i][sum1]=False
        return dp[i][sum1]
    n=len(arr)
    dp=[]
    for i in range(n):
        dp.append([-1]*(target+1))
    return solve(0,0,target,arr,dp)
    pass
    
    
    

