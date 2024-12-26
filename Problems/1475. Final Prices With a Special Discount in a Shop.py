class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = [0] * n
        for i in range(n-1):
            for j in range(i + 1, n):            
                if (prices[j] <= prices[i]):
                    answer[i] = prices[i] - prices[j]
                    break
                answer[i] = prices[i]
        answer[-1] = prices[-1]
        return answer