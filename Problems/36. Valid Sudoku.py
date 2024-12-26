class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkrow(board):
            for row in board:
                d = {}
                for item in row:
                    if item != ".":
                        if item in d :
                            return False
                        else :
                            d[item] = 1
            return True
        def checkcolumn(board):
            for i in range(0,9):
                d = {}
                for j in range(0,9):
                    if board[j][i] != ".":
                        if board[j][i] in d :
                            return False
                        else :
                            d[board[j][i]] = 1
            return True
        def check_sub_boxes(board):
            for i in range(1,9,3):
                for j in range(1,9,3):
                    d = {}
                    for x in range(i-1,i+2):
                        for y in range(j-1,j+2):
                            if board[x][y]!= ".":
                                if board[x][y] in d:
                                    return False
                                else:
                                    d[board[x][y]] = 1
            return True

        return checkrow(board) and checkcolumn(board) and check_sub_boxes(board)
