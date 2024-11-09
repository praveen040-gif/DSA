def assignMiceHoles(self, N , M , H):
    M.sort()
    H.sort()
    ans=float('-inf')
    for i in range(N):
        ans=max(ans,abs(M[i]-H[i]))
    return ans