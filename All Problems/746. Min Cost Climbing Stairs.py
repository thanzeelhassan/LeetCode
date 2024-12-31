class Solution:
    def helper(self,n,cost,dict1):
        if n in dict1:
            return dict1[n]
        if n < 0:
            dict1[n] = 0
            return 0
        if n == 0:
            dict1[n] = cost[n]
            return cost[n]
        if n == 1:
            dict1[n] = cost[n]
            return cost[n]

        temp = cost[n] + min(self.helper(n-1,cost,dict1), self.helper(n-2,cost,dict1))
        dict1[n] = temp
        return temp

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dict1 = {}
        return min(self.helper(n-1,cost,dict1),self.helper(n-2,cost,dict1))
