# Problem Description
 
 

# Given an array of integers A and an integer B.

# Find the total number of subarrays having bitwise XOR of all elements equals to B.



# Problem Constraints
# 1 <= length of the array <= 105

# 1 <= A[i], B <= 109



# Input Format
# The first argument given is the integer array A.

# The second argument given is integer B.



# Output Format
# Return the total number of subarrays having bitwise XOR equals to B.



# Example Input
# Input 1:

#  A = [4, 2, 2, 6, 4]
#  B = 6
# Input 2:

#  A = [5, 6, 7, 8, 9]
#  B = 5


# Example Output
# Output 1:

#  4
# Output 2:

#  2


# Example Explanation
# Explanation 1:

#  The subarrays having XOR of their elements as 6 are:
#  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
# Explanation 2:

#  The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left=0
        right=0
        sum1=0
        n=len(A)
        hashmap={}
        hashmap[0]=1
        ans=0
        while right<n:
            sum1=sum1^A[right]
            rem=sum1^B
            if rem in hashmap:
                ans+=hashmap[rem]
            if sum1 in hashmap:
                hashmap[sum1]+=1
            else:
                hashmap[sum1]=1
            right+=1
        return ans
                
            
