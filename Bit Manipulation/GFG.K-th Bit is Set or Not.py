#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        ans=1<<k
        res=ans & n
        if res!=0:
            return True
        return False
        #Your code here

#{ 
 # Driver Code Starts.


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        k=int(input())
        obj = Solution()
        if obj.checkKthBit(n,k):
            print("true")
        else:
            print("false")
        print("~")    
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends