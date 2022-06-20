class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def helper(matrix,n,m,i,j,temp):
            #print first row:
            for x in range(j,m):
                temp.append(matrix[i][x])
            #print last column:
            for x in range(i+1,n):
                temp.append(matrix[x][m-1])
            #print last row:
            if i != n-1:
                for x in range(m-2,j-1,-1):
                    temp.append(matrix[n-1][x])
            #print first column:
            if j != m-1 :
                for x in range(n-2,i,-1):
                    temp.append(matrix[x][j])

            i = i + 1
            j = j + 1
            n = n - 1
            m = m - 1
            if i < n and j < m:
                temp = helper(matrix,n,m,i,j,temp)

            return temp
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0
        temp = []
        temp = helper(matrix,n,m,i,j,temp)
        return temp
