def numJewelsInStones(self, jewels, stones):
    count=0
    for i in stones:
        if i in jewels:
            count=count+1
    return count