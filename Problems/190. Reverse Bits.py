class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            x = n & 1
            y = x ^ (out << 1)
            out = y
            n >>= 1
        return out
