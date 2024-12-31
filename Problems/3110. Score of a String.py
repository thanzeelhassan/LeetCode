class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(0, n - 1) :
            ascii_value_1 = ord(s[i])
            ascii_value_2 = ord(s[i+1])
            ans = ans + abs(ascii_value_1 - ascii_value_2)
        return ans