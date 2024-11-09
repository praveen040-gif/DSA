def canJump(self, nums: List[int]) -> bool:
    maxindex=0
    for i in range(len(nums)):
        if i>maxindex:
            return False
        else:
            maxindex=max(maxindex,i+nums[i])
            print(maxindex)
    return True