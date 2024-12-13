# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=""
        n=len(s)
        hashmap={}
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]]+=1
            else:
                hashmap[t[i]]=1
        left=0
        right=0
        count=len(hashmap)
        min1=float('inf')
        while right<n:
            if s[right] in hashmap:
                hashmap[s[right]]-=1
                if hashmap[s[right]]==0:
                    count-=1
            while count==0:
                res=right-left+1
                if res<min1:
                    ans=s[left:right+1]
                    min1=right-left+1
                if s[left] in hashmap:
                    hashmap[s[left]]+=1
                    if hashmap[s[left]]==1:
                        count+=1
                left+=1
            right+=1
        return ans


        