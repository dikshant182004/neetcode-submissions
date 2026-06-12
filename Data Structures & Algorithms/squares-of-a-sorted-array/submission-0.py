class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j =0, len(nums)-1
        ans=[]
        while(i<=j):
            # we are taling abs becz on square - -> + ve 
            if abs(nums[i]) < abs(nums[j]):
                ans.append(nums[j] ** 2)
                j-=1
            else:
                ans.append(nums[i]**2)
                i+=1

        return ans[::-1]