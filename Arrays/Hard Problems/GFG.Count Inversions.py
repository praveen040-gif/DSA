class Solution:
    def inversionCount(self, arr):
        def msort(arr,l,r):
            if l<r:
                mid=(l+r)//2
                msort(arr,l,mid)
                msort(arr,mid+1,r)
                merge(arr,l,mid,r)
        
        def merge(arr,l,mid,r):
            temp=[]
            left=l
            right=mid+1
            nonlocal count
            while left<=mid and right<=r:
                if arr[left]<=arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    count+=mid-left+1
                    right+=1
            while left<=mid:
                temp.append(arr[left])
                left+=1
            while right<=r:
                temp.append(arr[right])
                right+=1
            for i in range(l,r+1):
                arr[i]=temp[i-l]
        count=0
        msort(arr,0,len(arr)-1)
        return count

        
        # Your Code Here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends