class Solution:
    def helper(self,n,dict1):
        if n in dict1 :
            return dict1[n]
        if n == 0:
            dict1[n] = 0
            return 0
        if n == 1:
            dict1[n] = 1
            return 1
        if n == 2:
            dict1[n] = 2
            return 2

        temp = self.helper(n-1,dict1) + self.helper(n-2,dict1)
        dict1[n] = temp
        return temp

    def climbStairs(self, n: int) -> int:
        dict1 = {}
        return self.helper(n,dict1)
