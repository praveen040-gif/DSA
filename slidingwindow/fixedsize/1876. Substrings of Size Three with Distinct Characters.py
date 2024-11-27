# A string is good if there are no repeated characters.

# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

# A substring is a contiguous sequence of characters in a string.

 

# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".
# Example 2:

# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left=0
        right=0
        n=len(s)
        hashmap={}
        c=0
        while right<n:
            if s[right] in hashmap:
                hashmap[s[right]]+=1
            else:
                hashmap[s[right]]=1
            if right-left+1==3:
                if len(hashmap)==3:
                    c+=1
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            right+=1
        return c
        