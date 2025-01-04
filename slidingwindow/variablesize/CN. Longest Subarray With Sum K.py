# You are given an array 'a' of size 'n' and an integer 'k'.



# Find the length of the longest subarray of 'a' whose sum is equal to 'k'.



# Example :
# Input: ‘n’ = 7 ‘k’ = 3
# ‘a’ = [1, 2, 3, 1, 1, 1, 1]

# Output: 3

# Explanation: Subarrays whose sum = ‘3’ are:

# [1, 2], [3], [1, 1, 1] and [1, 1, 1]

# Here, the length of the longest subarray is 3, which is our final answer.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 7 3
# 1 2 3 1 1 1 1


# Sample Output 1 :
# 3


# Explanation Of Sample Input 1 :
# Subarrays whose sum = ‘3’ are:
# [1, 2], [3], [1, 1, 1] and [1, 1, 1]
# Here, the length of the longest subarray is 3, which is our final answer.


# Sample Input 2 :
# 4 2
# 1 2 1 3


# Sample Output 2 :
# 1


# Sample Input 3 :
# 5 2
# 2 2 4 1 2 


# Sample Output 3 :
# 1

def longestSubarrayWithSumK(arr: [int], k: int) -> int:
    right=0
    left=0
    n=len(arr)
    sum1=0
    max1=0
    while right<n:
        sum1+=arr[right]
        while sum1>k and left<n:
            sum1-=arr[left]
            left+=1
        if sum1==k:
            max1=max(max1,right-left+1)
        right+=1
    return max1
    
