#User function Template for python3

class Solution:
    def minimumEnergy(self, height, n):
        def allpossible(ind):
            right=float('inf')
            if ind==0:
                return 0
            left=allpossible(ind-1)+abs(height[ind]-height[ind-1])
            if ind>1:
                right=allpossible(ind-2)+abs(height[ind]-height[ind-2])
            return min(left,right)
        ans=allpossible(n-1)
        return ans
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
        print("~")
# } Driver Code Ends