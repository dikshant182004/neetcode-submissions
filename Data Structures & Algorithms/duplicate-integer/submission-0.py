class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for i in nums:
            if i in lookup : 
                return True 
            lookup.add(i)
        return False