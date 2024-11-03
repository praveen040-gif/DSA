def permutation(l,arr):
    if len(l)==len(arr):
        print("".join(l))
        return
    for i in range(len(arr)):
        if arr[i] not in l:
            l.append(arr[i])
            permutation(l,arr)
            l.pop()
arr=input()
l=[]
permutation(l,arr)

