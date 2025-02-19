class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        mi=prices[0]

        for i in range(1,len(prices)):
            mi=min(prices[i],mi)
            result=max(prices[i]-mi,result)
        return result
