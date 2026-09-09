class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        if n < 10000:
            return n - 1000 + 1
        if n <= 100000:
            return 9000 + n - 10000 + 1
