class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = [[float("INF") for i in range(n+1)] for j in range(m+1)]
        matrix[m-1][n] = 0
        matrix[m][n-1] = 0

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                matrix[j][i] = min(matrix[j+1][i],matrix[j][i+1]) + grid[j][i]

        return matrix[0][0]
