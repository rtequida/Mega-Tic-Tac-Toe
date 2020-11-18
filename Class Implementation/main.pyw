from tkinter import *
from tkinter.font import *
import random
from Player import Player
from Board import Board



def main():
    game = Game()

class Game:
    def __init__(self):
        self.MAIN_WIN_W = 500
        self.MAIN_WIN_H = 350
        self.GAME_WIN_W = 500
        self.GAME_WIN_H = 650
        self.COLOR = "forest green"
        root = Tk()
        root.config(cursor = "target")
        root.title("Mega Tic Tac Toe")
        mainFont = Font(family = "Helvetica", size = 36, underline = 1)
        secFont = Font(family = "Helvetica", size = 20)
        bFont = Font(family = "Helvetica", size = 18)
        canvas = Canvas(root, width = self.MAIN_WIN_W, height = self.MAIN_WIN_H, bg = self.COLOR)
        canvas.create_text(self.MAIN_WIN_W / 2, 50, text = "MEGA TIC TAC TOE", font = mainFont)
        canvas.create_text(self.MAIN_WIN_W / 2, 120, text = "Player's Names", font = mainFont)
        canvas.create_text(self.MAIN_WIN_W / 5, 200, text = "Player 1:", font = secFont)
        canvas.create_text(self.MAIN_WIN_W / 5, 240, text = "Player 2:", font = secFont)
        p1 = Entry(canvas)
        p1.place(x = 160, y = 200, width = 295, height = 25, anchor = W)
        p2 = Entry(canvas)
        p2.place(x = 160, y = 240, width = 295, height = 25, anchor = W)
        submit = Button(canvas, text = "Start Game", font = bFont, command = lambda: self.playerSetup(root, p1, p2))
        submit.place(x = self.MAIN_WIN_W / 2, y = 303, anchor = CENTER)
        canvas.grid()

        root.mainloop()

    def playerSetup(self, root, p1, p2):
        player1 = Player(p1.get())
        player2 = Player(p2.get())
        player1.setP2(player2)
        players = [player1, player2]
        root.destroy()
        self.startGame(players)

    def startGame(self, players):
        game_root = Tk()
        game_root.config(cursor = "target")
        game_root.title("Mega Tics Tac Toe")
        game_root.config(bg = self.COLOR)
        game_root.geometry(str(self.GAME_WIN_W) + "x" + str(self.GAME_WIN_H))
        mFont = Font(family = "Helvetica", size = 36)
        bFont = Font(family = "Helvetica", size = 18)
        r = random.randint(0, 1)
        players[0].setMark(r)
        curr_player = players[r].getTitle()
        canvas = Canvas(game_root, width = self.GAME_WIN_W, height = 80, bg = self.COLOR, highlightthickness = 0)
        canvas.create_text(self.GAME_WIN_W / 2, 40, text = curr_player, font = mFont)
        board = Board(self, game_root, players, canvas)
        bottom = Frame(game_root, bg = self.COLOR)
        restart = Button(bottom, text = "Start Over", font = bFont, command = lambda: self.restartProcess(players, game_root))
        restart.grid(pady = 25)

        canvas.pack()
        board.getBoard().pack()
        bottom.pack()

        game_root.mainloop()

    def restartProcess(self, players, game_root):
        game_root.destroy()
        self.startGame(players)

    def processChoice(self, choice, root, players):
        root.destroy()
        if choice == 0:
            self.startGame(players)
        else:
            game = Game()

main()
