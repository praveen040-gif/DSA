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