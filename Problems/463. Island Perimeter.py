class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid) #rows
        n = len(grid[0]) #columns
        matrix = [[0 for i in range(n+2)] for j in range(m+2)]
        result = 0
        for i in range(0,m):
            for j in range(0,n):
                matrix[i+1][j+1] = grid[i][j]
        #add horizontal
        for i in range(1,m+2):
            for j in range(1,n+2):
                if matrix[i][j] != matrix[i][j-1]:
                    result+=1
        #add vertical
        for i in range(1,n+2):
            for j in range(1,m+2):
                if matrix[j][i] != matrix[j-1][i]:
                    result+=1
        return result
