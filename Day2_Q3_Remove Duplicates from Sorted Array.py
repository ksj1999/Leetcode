# Error 1. index out of range error
# 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                nums[k] = nums[i]
                k+=1
        return k
