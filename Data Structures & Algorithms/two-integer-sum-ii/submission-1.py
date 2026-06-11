class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we can't use hm as it req O(1) space 
        # plus we can use the fact that array is sorted 
        l,r = 0, len(numbers)-1
        while(l<r):
            sum= numbers[l]+numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1,r+1]
        return []



