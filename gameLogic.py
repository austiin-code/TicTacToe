import pygame


class TicTacToe:
    def __init__(self):
        self.board = [[None] * 3 for i in range(3)]
        self.turn = 'X'
        self.winner = None
        self.winLineStart = None
        self.winLineEnd = None
        self.draw = False

    def makeMove(self, row, col):
        if self.board[row][col] is None and not self.winner:
            self.board[row][col] = self.turn
            self.checkWinner()
            self.turn = 'O' if self.turn == 'X' else 'X'

    def checkWinner(self):
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None: #checks columns for same letter
                self.winner = self.board[0][i] #assigns variable with X or O depending on who won
                self.winLineStart = (i * 200 + 99.5, 12)
                self.winLineEnd = (i * 200 + 99.5, 588)
                return
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None: #checks rows for same letter
                self.winner = self.board[i][0]
                self.winLineStart = (12, i * 200 + 99.5)
                self.winLineEnd = (588, i * 200 + 99.5)
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None: #checks left diagonal for same letter
            self.winner = self.board[0][0]
            self.winLineStart = (12, 12)
            self.winLineEnd = (588, 588)
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None: #checks right diagonal for same letter
            self.winner = self.board[0][2]
            self.winLineStart = (12, 588)
            self.winLineEnd = (588, 12)
            return
        if all(cell is not None for row in self.board for cell in row) and self.winner is None:
            self.draw = True