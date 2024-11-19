def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    left=0
    right=0
    max1=0
    sum1=0
    hashmap={}
    while right<len(nums):
        sum1=sum1+nums[right]
        if nums[right] in hashmap:
            hashmap[nums[right]]+=1
        else:
            hashmap[nums[right]]=1
        # print(hashmap)
        if (right-left)+1==k:
            if len(hashmap)==k:
                max1=max(sum1,max1)
                sum1=sum1-nums[left]
                hashmap[nums[left]]-=1
                if hashmap[nums[left]]==0:
                    del hashmap[nums[left]]
                left+=1
            else:
                sum1=sum1-nums[left]
                hashmap[nums[left]]-=1
                if hashmap[nums[left]]==0:
                    del hashmap[nums[left]]
                left+=1

        right+=1
    return max1