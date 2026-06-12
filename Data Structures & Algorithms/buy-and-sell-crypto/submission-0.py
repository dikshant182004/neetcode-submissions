class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        buy=prices[0]
        for i in prices:
            if i< buy: # buy at cheap rate 
                buy=i
            else:
                max_profit=max(max_profit,i-buy)
        return max_profit