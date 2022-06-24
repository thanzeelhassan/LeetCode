class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        x = math.log10(n)/ math.log10(3)
        ans = pow(3,int(x))
        if ans == n:
            return 1
        return 0