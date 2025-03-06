class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        values = [0] * (n*n + 1)
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                temp = grid[i][j] 
                if values[temp] == 0:
                    values[temp] = 1
                elif values[temp] == 1:
                    a = temp
                    values[temp] = 2
        for i in range(1, n*n + 1):
            if values[i] == 0:
                b = i
        return [a, b]
