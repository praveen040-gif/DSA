# Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

# Example 1:

# Input:
# txt = forxxorfxdofr
# pat = for
# Output: 3
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.
# Example 2:

# Input:
# txt = aabaabaa
# pat = aaba
# Output: 4
# Explanation: aaba is present 4 times
# in txt.
# Your Task:
# Complete the function search() which takes two strings pat, txt, as input parameters and returns an integer denoting the answer. 
# You don't need to print answer or take inputs.

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(26) or O(256)
#User function Template for python3
	
def search(pat, txt):
        n=len(txt)
        hashmap={}
        for i in pat:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        count=len(hashmap)
        right=0
        left=0
        c=0
        while right<n:
            if txt[right] in hashmap:
                hashmap[txt[right]]-=1
                if hashmap[txt[right]]==0:
                    count-=1
            if right-left+1==len(pat):
                if count==0:
                    c+=1
                if txt[left] in hashmap:
                    hashmap[txt[left]]+=1
                    if hashmap[txt[left]]==1:
                        count+=1
                left+=1
            right+=1
        return c
	               
	        





if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ans = search(pat, txt)
        print(ans)
        tc=tc-1
        print("~")
