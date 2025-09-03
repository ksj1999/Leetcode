class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False
--------------------------------------------


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False


--------------------------------------------


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
