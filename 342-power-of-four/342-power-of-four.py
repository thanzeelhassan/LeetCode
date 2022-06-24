class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        x = math.log10(n)/ math.log10(4)
        ans = pow(4,int(x))
        if ans == n:
            return 1
        return 0