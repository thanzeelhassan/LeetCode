class Solution:
    def helper(self,n,dp):
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            return 0
        result = float("INF")
        for i in range(1,int(sqrt(n)+1)):
            result = min(result, 1 + self.helper(n-i*i,dp))
        dp[n] = result
        return result
    def numSquares(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.helper(n,dp)
