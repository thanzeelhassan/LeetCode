class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        matrix2 = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                matrix2[i][j] = matrix[i][j]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # change row
                    for k in range(0,m):
                        matrix2[k][j] = 0
                    # change column
                    for k in range(0,n):
                        matrix2[i][k] = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = matrix2[i][j]
        
