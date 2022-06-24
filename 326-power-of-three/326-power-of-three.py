class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.isPowerOfThree(n/3)
        