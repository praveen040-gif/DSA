def maxVowels(self, s: str, k: int) -> int:
    n=len(s)
    right=0
    left=0
    v="aeiou"
    max1=0
    count=0
    while right<n:
        if s[right] in v:
            count=count+1
        right=right+1
        if right-left==k:
            max1=max(max1,count)
            if s[left] in v:
                count-=1
            left+=1
    return max1