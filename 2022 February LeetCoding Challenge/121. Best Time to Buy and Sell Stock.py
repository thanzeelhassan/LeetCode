class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            elif prices[i] > prices[buy]:
                profit = prices[i] - prices[buy]
                if profit > max_profit:
                    sell = i
                    max_profit = profit

        return max_profit
