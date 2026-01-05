class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        count = 0
        sum_total = 0
        min_value = abs(matrix[0][0])
        for row in matrix:
            for item in row:
                sum_total = sum_total + abs(item)
                if item < 0:
                    count = count + 1
                min_value = min(min_value, abs(item))
        if count % 2 == 0:
            return sum_total
        else:
            return sum_total - 2 * min_value  
