class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top = []
        side = []
        r = len(grid)
        c = len(grid[0])
        # side has all the max elements on each row
        for item in grid:
            side.append(max(item))
        # top has all the max elements on each column
        for i in range(c):
            temp = float("-INF")
            for j in range(r):
                if grid[j][i] > temp:
                    temp = grid[j][i]
            top.append(temp)
        #min max
        result = 0
        for i in range(r):
            for j in range(c):
                result = result + min(side[i], top[j]) - grid[i][j]
        return result



        
