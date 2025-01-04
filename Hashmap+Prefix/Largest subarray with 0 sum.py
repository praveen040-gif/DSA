# Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.

# Examples:

# Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation: The largest subarray with a sum of 0 is [-2, 2, -8, 1, 7].
# Input: arr[] = [2, 10, 4]
# Output: 0
# Explanation: There is no subarray with a sum of 0.
# Input: arr[] = [1, 0, -4, 3, 1, 0]
# Output: 5
# Explanation: The subarray is [0, -4, 3, 1, 0].

#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        right=0
        n=len(arr)
        sum1=0
        max1=0
        hashmap={}
        while right<n:
            sum1+=arr[right]
            if sum1==0:
                max1=max(max1,right+1)
            if sum1 in hashmap:
                max1=max(max1,right-hashmap[sum1])
            if sum1 not in hashmap:
                hashmap[sum1]=right
            right+=1
        return max1
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends