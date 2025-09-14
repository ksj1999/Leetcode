class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set()
        for i in nums:
            for j in nums:
                if i+1 == j:
                    seq.add(i)
                    seq.add(j)
        sortedseq = sorted(seq)
        return len(sortedseq)


-----------------------------


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0

        for i in seq:
            if i-1 not in seq:
                length = 1
                while i + length in seq:
                    length += 1
                longest = max(longest, length)
        return longest
