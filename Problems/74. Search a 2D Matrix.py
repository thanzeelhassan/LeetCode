class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = []
        for i in range(len(matrix)):
            start.append(matrix[i][0])
        i = 0
        while(i < len(start)):
            if target < start[i]:
                break
            i = i + 1
        x = i-1
        for i in range(len(matrix[0])):
            if target == matrix[x][i]:
                return True
        return False
