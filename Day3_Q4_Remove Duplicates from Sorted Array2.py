# Error 1. Out of Index Error
# Reason: Updated K on all situations. Should not update K in else case.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = 0
        for i in range(1, len(nums)):
            print(nums)
            if nums[i] != nums[k-1]:
                nums[k-1] = nums[i]
                k+=1
            else:
                count+=1
                k+=1
                if count>=2:
                    nums[k-1] = nums[i]
                    k+=1
                    count = 0

----------------------------------------------
# Error 2. Assigning nums[k-1] disrupts the already assigned values.
# Solution: Should assign on nums[k]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = 0
        for i in range(1, len(nums)):
            print(nums)
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
            else:
                count+=1
                if count>=2:
                    nums[k] = nums[i]
                    k+=1
                    count = 0

----------------------------------------------
# Error 3. Count keeps going up
# Reason: Did not update count to 0 after value change.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = 0
        for i in range(1, len(nums)):
            print(nums)
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k+=1
            else:
                count+=1
                if count>=2:
                    nums[k] = nums[i]
                    k+=1
                    count = 0

-------------------------------------------------------



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[k-1]:
                if count < 2:
                    nums[k] = nums[i]
                    k += 1
                    count += 1
            else:
                nums[k] = nums[i]
                k += 1
                count = 1
        
        return k

----------


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k+=1
        
        return k
