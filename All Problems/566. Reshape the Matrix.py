class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        result = [[0 for i in range(c)] for j in range(r)]
        print(result)
        l = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                l.append(mat[i][j])
        x = 0
        for i in range(r):
            for j in range(c):
                result[i][j] = l[x]
                x = x + 1
        return result
