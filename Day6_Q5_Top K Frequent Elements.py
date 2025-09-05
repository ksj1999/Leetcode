# Try 1. Tried to use dictionary to store unique num & count
# Error: When using sorted() on a Dict, it sorts the biggest Key not Values. So I'm not sorting the biggest frequency, just the biggest key number.
# Error: .pop() function pops the value from Dict. In my case I want to pop the key.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = set(nums)
        rankmap = {}
        for i in numset:
            count = -1
            for j in nums:
                if i == j:
                    count += 1
                    rankmap[i] = count
            print(rankmap)

        output = []
        sortedrank = sorted(rankmap)


        for n in range(k):
            output.append(sortedrank.pop())
        
        return output

------------------------------------------------------

# Try 2. Tried to change the key, values: rankmap[i] = count -> rankmap[count] = i
# Error: Whenever there is the same count, it resets the keys.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = set(nums)
        rankmap = {}
        for i in numset:
            count = -1
            for j in nums:
                if i == j:
                    count += 1
                    rankmap[count] = i
            print(rankmap)

        output = []
        sortedrank = sorted(rankmap)


        for n in range(k):
            output.append(sortedrank.pop())
        
        return output
------------------------------------------------------

# Try 3. Using Tuple to store key value, and sort by value
# Side note: I don't think I needed to use Tuple to solve the issue. Just needed to sort by value.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numset = set(nums)
        rankmap = {}
        for i in numset:
            count = -1
            for j in nums:
                if i == j:
                    count += 1
                    rankmap[i] = count
            print(rankmap)

        sortedrank = sorted(rankmap.items(), key=lambda x: x[1])

        output = []
        for _ in range(k):
            output.append(sortedrank.pop()[0])
        
        return output

-----------------------














