class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            return [0]*len(nums)

        product=math.prod(nums)
        product_without_0=1
        for i in nums:
            if i==0:
                continue
            product_without_0 *= i

        ans=[]
        for i in nums:
            if i==0:
                ans.append(product_without_0)
            else:
                ans.append(int(product/i))

        return ans