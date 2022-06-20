class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        result = 0
        for i in range(1,n+1):
            result += self.numTrees(i-1) * self.numTrees(n-i)
        return result
