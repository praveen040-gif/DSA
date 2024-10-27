def majorityElement(self, nums: List[int]) -> int:
    n=len(nums)
    hashmap={}
    for i in range(n):
        if nums[i] in hashmap:
            hashmap[nums[i]]+=1
        else:
            hashmap[nums[i]]=1
    for i in hashmap:
        if hashmap[i]>n//2:
            return i