class Solution:
    def minOperations(self, n: int) -> int:
        result = 0        
        for i in range(1,n,2):
            result = result + (n-i)
        return result