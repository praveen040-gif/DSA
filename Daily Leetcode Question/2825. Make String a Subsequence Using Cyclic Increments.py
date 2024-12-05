class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n=len(str1)
        j=0
        for i in range(n):
            x=ord(str1[i])
            if x==122:
                if (chr(x) ==str2[j]) or (chr(97) == str2[j]):
                    j+=1
            else:
                # print(chr(x),chr(x+1))
                if(chr(x) == str2[j]) or (chr(x+1)==str2[j]):
                    j+=1
                    # print(c)
            if j==len(str2):
                return True
        return False

        