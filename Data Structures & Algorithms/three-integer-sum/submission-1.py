class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i >0 and a == nums[i-1]:
                # becz it will share the same PNC
                continue 
            l,r= i+1, len(nums)-1
            while (l<r):
                sum = a+ nums[l]+nums[r]
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l +=1 # just to proceed furthur to add more triplets
                    # [-2,-2,0,2,2] l=-2, r=2
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                        # just need to proceed 1 pointer either l or r for P&c
                        # rest will get handled by above one 

        return ans