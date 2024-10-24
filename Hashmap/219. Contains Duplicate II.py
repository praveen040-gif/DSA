def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    n=len(nums)
    right=0
    left=0
    hashmap={}
    while right<n:
        if nums[right] in hashmap:
            print()
            ans=abs(right-hashmap[nums[right]])
            if ans<=k:
                return True
        hashmap[nums[right]]=right
        right=right+1
    return False