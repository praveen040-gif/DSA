# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        right=0
        hashmap={}
        max1=0
        while right<n:
            if s[right] in hashmap:
                hashmap[s[right]]+=1
            else:
                hashmap[s[right]]=1
            while len(hashmap)!=right-left+1:
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            max1=max(max1,right-left+1)
            right+=1
        return max1
        