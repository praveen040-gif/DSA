# 
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n=len(s)
        left=0
        right=0
        c=0
        s1="aeiou"
        max1=0
        while right<n:
            if s[right] in s1:
                c+=1
            if right-left+1==k:
                max1=max(max1,c)
                if s[left] in s1:
                    c-=1
                left+=1
            right+=1
        return max1

        