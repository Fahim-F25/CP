from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        bestBuy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] > bestBuy:
                maxProfit = max(maxProfit, prices[i] - bestBuy)
            bestBuy = min(bestBuy, prices[i])

        return maxProfit

prices = list(map(int, input().split()))
print(Solution().maxProfit(prices))