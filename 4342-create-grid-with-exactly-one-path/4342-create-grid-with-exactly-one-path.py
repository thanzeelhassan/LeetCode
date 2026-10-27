class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(0,m):
            for j in range(0,n):
                arr[i][j] = '#'

        for i in range(0,n):
            arr[0][i] = '.'

        for i in range(0,m):
            arr[i][-1] = '.'

        result = []

        temp = ""

        for i in range(0,m):
            for j in range(0,n):
                temp = temp + arr[i][j]
            result.append(temp)
            temp = ""

        return result