class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        temp = []
        k = 1
        for i in nums:
            k = k*i
        
        for j in nums:
            if j != 0:
                n = k / j
                temp.append(int(n))
            else:
                temp.append(0)
        return temp
------------------------------------

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        k = 1
        for i in nums:
            if i != 0:
                k *= i

        if zero_count == 0:
            for j in nums:
                temp.append(k // j)  # integer division avoids float issues
        else:
            for j in nums:
                if j == 0:
                    temp.append(k)
                else:
                    temp.append(0)

        return temp


-------------------------------------------------------------------



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        temp = []

        for i in range(len(nums)):
            k = 1

            for j in range(len(nums)):
                if i != j:
                    k = k*nums[j]

            temp.append(k)
        
        return temp


----------------------------------

