from tkinter import *
from tkinter.font import *

class Tile:
    def __init__(self, but_num, sec_num, parent, board):
        button_overrelief = "groove"
        font = 20
        h = 2
        w = 4
        self.but_num = but_num
        self.sec_num = sec_num
        self.parent = parent
        self.board = board
        self.me = Button(self.parent, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: self.board.process(but_num, sec_num, self.me))
        self.me.grid(row = int(but_num / 3), column = int(but_num % 3))
