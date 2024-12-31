class Solution:
    def check_winner(self,board):
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return board[0][0]
        if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            return board[2][0]
        for i in range(3):
            temp = board[i][0]
            flag = 1
            for j in range(3):
                if board[i][j] ==temp:
                    continue
                else:
                    flag = 0
            if flag == 1:
                return temp
        for i in range(3):
            temp = board[0][i]
            flag = 1
            for j in range(3):
                if board[j][i] ==temp:
                    continue
                else:
                    flag = 0
            if flag == 1:
                return temp
        return 0
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["_" for i in range(3)] for j in range(3)]
        flag = 0
        for move in moves:
            if flag == 0:
                board[move[0]][move[1]] = "X"
                flag = 1
            elif flag == 1:
                board[move[0]][move[1]] = "O"
                flag = 0

            temp2 = self.check_winner(board)
            if temp2 == "X":
                return "A"
            elif temp2 == "O":
                return "B"
        if len(moves) < 9:
            return "Pending"
        return "Draw"
