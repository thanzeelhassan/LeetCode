class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * (pow(n - 1, 2)) + (2 * n) - 1