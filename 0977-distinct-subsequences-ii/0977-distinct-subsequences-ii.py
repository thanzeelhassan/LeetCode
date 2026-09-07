class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        dp = [0] * 26

        for c in s :
            c = ord(c) - 97
            new = total + 1 - dp[c]
            total = (total + new) % MOD
            dp[c] = (dp[c] + new) % MOD

        return total % MOD