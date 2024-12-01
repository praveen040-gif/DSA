from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    def solve(i,sum1,total):
        if i>=n:
            s1=sum1
            s2=total-sum1
            if s1>=s2:
                if abs(s1-s2)==d:
                    return 1
                return 0
            return 0
        if dp[i][sum1]!=-1:
            return dp[i][sum1]
        pick=solve(i+1,sum1+arr[i],total)%(10**9+7)
        notpick=solve(i+1,sum1,total)%(10**9+7)
        dp[i][sum1]=(pick+notpick)%(10**9+7)
        return dp[i][sum1]
    total=sum(arr)
    dp=[]
    for i in range(n):
        dp.append([-1]*(total+1))
    return solve(0,0,total)

            

    pass
