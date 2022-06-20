class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        array = []
        buy = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            elif prices[i] > prices[buy]:
                profit = prices[i] - prices[buy]
                array.append(profit)
                buy = i

        return sum(array)
