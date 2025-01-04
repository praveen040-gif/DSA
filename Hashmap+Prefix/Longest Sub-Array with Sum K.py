# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        right=0
        n=len(arr)
        sum1=0
        max1=0
        hashmap={}
        while right<n:
            sum1+=arr[right]
            if sum1==k:
                max1=max(max1,right+1)
            ans=sum1-k
            # print(ans)
            if ans in hashmap:
                max1=max(max1,right-hashmap[ans])
            if sum1 not in hashmap:
                # print(sum1,right)
                hashmap[sum1]=right
            right+=1
        return max1
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends