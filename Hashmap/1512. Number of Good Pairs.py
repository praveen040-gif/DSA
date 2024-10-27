def numIdenticalPairs(self, nums: List[int]) -> int:
    hashmap={}
    ans=0
    for i in range(len(nums)):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
            ans=ans+hashmap[nums[i]]-1
        else:
            hashmap[nums[i]]=1
    return ans