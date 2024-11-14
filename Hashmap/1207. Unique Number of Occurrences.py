def uniqueOccurrences(self, arr: List[int]) -> bool:
    hashmap={}
    # arr.sort()
    for i in range(len(arr)):
        if arr[i] in hashmap:
            hashmap[arr[i]]+=1
        else:
            hashmap[arr[i]]=1
    l=[]
    for i in hashmap.values():
        if i in l:
            return False
        l.append(i)
    return True