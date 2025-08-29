# Error 1. Use Del list or Remove() function
# Reason : Number of list got reduced by del or remove() function
# Note : del list / list.remove() does not make a copy like slicing does. It operates on the list itself.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val == nums[i]:
                print(val, nums[i])
                del nums[i]
                print(nums)
        k = len(nums)


# Fix 1. Use Del without changing the index of list
# Method : Remove from the back of the list
# Overall bad idea..

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1, -1, -1):
            if val == nums[i]:
                print(val, nums[i])
                del nums[i]
                print(nums)
        k = len(nums)

# Upgrade 3. Using While so that the index doesn't matter.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val) 
        return len(nums)


# Final Solution. Two Pointer problem
# This method is opposite of what I have done(focusing on when the val and num[] is same) as it focuses when the val and num[] is different.
# Use K and I to replace whenever the value is different.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for i in range(len(nums)):
            print(nums)
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
