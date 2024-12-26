class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diags = collections.defaultdict(list)
        for i,row in enumerate(mat):
            for j, a in enumerate(row):
                diags[i-j].append(a)  
        
        for diag in diags.values():
            diag.sort(reverse = True)
        
        for i,row in enumerate(mat):
            for j, _ in enumerate(row):
                mat[i][j] = diags[i-j].pop()

        return mat
        