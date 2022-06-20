class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while int(r*r) > x:
            r = (r + x/r) / 2
        return int(r)
        
