from tkinter import *
from Tile import Tile

class Section:
    def __init__(self, i, parent, board):
        frame_relief = "solid"
        bd = 3
        self.num = i
        self.parent = parent
        self.board = board
        self.me = Frame(parent, relief = frame_relief, bd = bd)
        self.me.grid(row = int(self.num / 3), column = int(self.num % 3))
        for x in range(9):
            tile = Tile(x, i, self.me, self.board)
        self.won = 0
        self.winner = ""
        self.count = 0

    def setWinner(self, player):
        self.won = 1
        self.winner = player

    def incrCount(self):
        self.count += 1

    def getSection(self):
        return self.me

    def getWon(self):
        return self.won

    def getWinner(self):
        return self.winner

    def getCount(self):
        return self.count
