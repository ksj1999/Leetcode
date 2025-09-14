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


