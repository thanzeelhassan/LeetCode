class Solution:
    def helper(self,m,n,dict1):
        temp = str(m) + "_" + str(n)
        if temp in dict1:
            return dict1[temp]
        
        if m == 1:
            dict1[temp] = 1
            return 1
        if n == 1:
            dict1[temp] = 1
            return 1
        value = self.helper(m-1,n,dict1) + self.helper(m,n-1,dict1)
        dict1[temp] = value
        return value
    def uniquePaths(self, m: int, n: int) -> int:
        dict1 = {}
        return self.helper(m,n,dict1)