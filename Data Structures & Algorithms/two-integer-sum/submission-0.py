class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict ={}
        for i,n in enumerate(nums):
            rem = target-n
            if rem in map_dict:
                return [map_dict[rem], i]
            map_dict[n]=i  # i -> index ,n -> value 
        