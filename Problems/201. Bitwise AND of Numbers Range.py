class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        k = 0
        while left != right:
            left >>= 1
            right >>= 1
            k += 1
        return left << k    
