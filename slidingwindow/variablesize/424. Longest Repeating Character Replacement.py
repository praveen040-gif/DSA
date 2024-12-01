# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def ispossible(limit):
            hashmap={}
            n=len(s)
            right=0
            left=0
            while right<n:
                if s[right] in hashmap:
                    hashmap[s[right]]+=1
                else:
                    hashmap[s[right]]=1
                if right-left+1==limit:
                    ans=max(hashmap.values())
                    if ans+k>=limit:
                        return True
                    hashmap[s[left]]-=1
                    if hashmap[s[left]]==0:
                        del hashmap[s[left]]
                    left+=1
                right+=1
            return False
        low=1
        high=len(s)
        while low<=high:
            mid=(low+high)//2
            if ispossible(mid):
                low=mid+1
            else:
                high=mid-1
        return high

        