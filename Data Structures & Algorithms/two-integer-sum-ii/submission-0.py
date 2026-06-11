class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm ={}
        for i, n in enumerate(numbers):
            rem = target -n
            if rem in hm:
                return [hm[rem]+1,i+1]
            hm[n]=i
        