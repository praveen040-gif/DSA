# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l=[] 
        ans=1
        n=rowIndex+1
        num=n
        den=n
        l.append(ans)
        for i in range(1,n):
            num=num*(n-i)
            den=den*i
            ans=num//den
            l.append(ans)
        return l


        