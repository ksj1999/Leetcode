# Try 1. Use Del list or Remove() function
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


# Try 2. Use Del without changing the index of list
# 

