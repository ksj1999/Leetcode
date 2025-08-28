# Error 1. Try using slicing and sort() function.
# Reason: .sort() by default returns None. -> which is why print(nums1) looks fine but at the end prints none 

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[0:m]
        nums1 = (nums1+nums2).sort()

-------------------------------------------------------------------------------------------------------------

# Error 2. Change to sorted(num1) but still didn't change the final output in IDE.
# Reason: When slicing a list it automatically makes a new one. -> nums1 = nums1[sliced] makes a new copy of original list nums1 and names it nums1
# basically all the function below just chages the new variable nums1 and never touches the original nums1 memory. 

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[0:m]
        nums1 = (nums1+nums2)
        print(nums1)
        nums1 = sorted(nums1)
        print(nums1)
