class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        size = m * n + 1
        array = [0] * size
        for i in range(m):
            for j in range(n):
                temp = mat[i][j]
                array[temp] = [i,j]

        rows_zero_status = [n] * m
        columns_zero_status = [m] * n

        l = len(arr)
        for i in range(l):
            val = arr[i]
            u, v = array[val][0], array[val][1]
            mat[u][v] = 0
            rows_zero_status[u] = rows_zero_status[u] - 1
            columns_zero_status[v] = columns_zero_status[v] - 1

            if rows_zero_status[u] == 0:
                return i
            if columns_zero_status[v] == 0:
                return i

        return l