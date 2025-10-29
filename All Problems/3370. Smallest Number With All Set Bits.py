class Solution:
    def smallestNumber(self, n: int) -> int:
        count = 0
        while(n > 0):
            n = n // 2
            count = count + 1

        return pow(2, count) - 1