def solve(self, bt):
    bt.sort()
    n=len(bt)
    curr=0
    prev=0
    for i in range(n):
        curr=curr+prev
        prev=prev+bt[i]
    return curr//n