class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        longest=0
        for i in nums:
            if (i-1) not in new: # marking the start of the seqn
                length = 0
                while(i+length) in new:
                    length += 1
                longest = max(length, longest)
        return longest    
