from functools import lru_cache
class Solution:
    @lru_cache(None)
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return s
        if len(s) == 1:
            return s
        if s == s[::-1]:
            return s
        else:
            s1 = self.longestPalindrome(s[1:])
            s2 = self.longestPalindrome(s[:-1])
            if len(s1) > len(s2):
                return s1
            else:
                return s2
