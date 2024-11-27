# Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
def findAnagrams(s, p):
    hashmap1={}
    k=len(p)
    for i in range(k):
        if p[i] in hashmap1:
            hashmap1[p[i]]+=1
        else:
            hashmap1[p[i]]=1
    hashmap2={}
    n=len(s)
    right=0
    left=0
    l=[]
    while right<n:
        if s[right] in hashmap2:
            hashmap2[s[right]]+=1
        else:
            hashmap2[s[right]]=1
        if right-left+1==k:
            print(hashmap1,hashmap2)
            if hashmap1==hashmap2:
                l.append(left)
            hashmap2[s[left]]-=1
            if hashmap2[s[left]]==0:
                del hashmap2[s[left]]
            left=left+1
        right=right+1
    return l
