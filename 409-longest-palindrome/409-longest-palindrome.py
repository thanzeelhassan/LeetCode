class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the letters which occur odd number of times
        if len(hash) > 0:
            return len(s) - len(hash) + 1
        return len(s)
