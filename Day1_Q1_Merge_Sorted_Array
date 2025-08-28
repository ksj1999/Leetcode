# Error 1. Try using slicing and sort() function.
# Reason: .sort() by default returns None. -> which is why print(nums1) looks fine but at the end prints none 

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[0:m]
        nums1 = (nums1+nums2).sort()
