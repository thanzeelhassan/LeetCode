class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        result = [[0 for _ in range(rows)] for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                result[j][i] = matrix[i][j]
        return result