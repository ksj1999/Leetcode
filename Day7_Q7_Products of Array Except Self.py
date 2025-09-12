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
