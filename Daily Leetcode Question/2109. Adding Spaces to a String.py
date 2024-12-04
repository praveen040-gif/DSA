class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k=0
        s1=""
        for space in spaces:
            s1=s1+s[k:space]
            s1=s1+" "
            k=space
        s1=s1+s[space:]
        return s1
        