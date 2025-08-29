# Error 1. index out of range error

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                nums[k] = nums[i]
                k+=1
        return k

# Final Solution
# Start from 1 because first element is always unique and k-1 stops from index error.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
        return k
            
