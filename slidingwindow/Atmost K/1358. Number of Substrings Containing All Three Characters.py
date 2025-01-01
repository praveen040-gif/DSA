# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

def numberOfSubstrings(self, s: str) -> int:
    def atmostk(s,k):
        n=len(s)
        ans=0
        right=0
        left=0
        hashmap={}
        while right<n:
            if s[right] in hashmap:
                hashmap[s[right]]+=1
            else:
                hashmap[s[right]]=1
            while len(hashmap)>k:
                hashmap[s[left]]-=1
                if hashmap[s[left]]==0:
                    del hashmap[s[left]]
                left+=1
            ans+=right-left+1
            right+=1
        return ans
    return atmostk(s,3)-atmostk(s,2)