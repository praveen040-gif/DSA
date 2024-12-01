# Perfect Sum Problem
# Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

# Note: It is guaranteed that the product of the length of arr and target will not exceed 106

# Examples:

# Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
# Output: 3
# Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.
# Input: arr[] = [2, 5, 1, 4, 3], target = 10
# Output: 3
# Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.
# Input: arr[] = [5, 7, 8], target = 3
# Output: 0
# Explanation: There are no subsets of the array that sum up to the target 3.
# Input: arr[] = [35, 2, 8, 22], target = 0
# Output: 1
# Explanation: The empty subset is the only subset with a sum of 0.
# Constraints:
# 1 ≤ arr.size() ≤ 103
# 0 ≤ arr[i] ≤ 103
# 0 ≤ target ≤ 103
from typing import List

def findWays(arr: List[int], k: int) -> int:
    def solve(i, sum1):
        if sum1 > k:  # If the current sum exceeds k, no solution is possible
            return 0
        if i == len(arr):  # If all elements are considered
            if sum1 == k:
                return 1
            return 0
        if dp[i][sum1] != -1:  # Return memoized result if available
            return dp[i][sum1]
        
        # Pick the current element
        pick1 = solve(i + 1, sum1 + arr[i])%(10**9+7)
        # Do not pick the current element
        pick2 = solve(i + 1, sum1)%(10**9+7)
        
        # Store the result in dp
        dp[i][sum1] = (pick1+pick2) %(10**9+7)
        return dp[i][sum1]
    
    # Initialize dp table with -1
    dp = [[-1] * (k + 1) for _ in range(len(arr))]
    return solve(0, 0)

