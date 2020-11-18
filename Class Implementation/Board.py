from tkinter import *
from tkinter.font import *
from Section import Section
from Player import Player

class Board:
    def __init__(self, game, root, players, canvas):
        self.game = game
        self.root = root
        self.board = Frame(root)
        self.players = players
        self.canvas = canvas
        self.sections = [None,None,None,None,None,None,None,None,None]
        for i in range(9):
            self.sections[i] = Section(i, self.board, self)
        self.COLOR = "forest green"
        self.MAIN_WIN_W = 500
        self.MAIN_WIN_H = 350

    def process(self, but_num, sec_num, button):
        DIS_BACK = "gray70"
        DIS_FONT = "black"
        DEF_COLOR = "gray90"
        WIN_COLOR = "red"
        GAME_WIN_W = 500
        mark_font = Font(family = "Helvetica", size = 80)
        mFont = Font(family = "Helvetica", size = 36)
        curr_mark = ""
        sec_win = 0
        if self.players[0].getTurn() == 1:
            curr_mark = self.players[0].getMark()
            new_turn_player = self.players[1]
        else:
            curr_mark = self.players[1].getMark()
            new_turn_player = self.players[0]
        self.players[0].switchTurns()
        self.canvas.delete("all")
        self.canvas.create_text(GAME_WIN_W / 2, 40, text = new_turn_player.getTitle(), font = mFont)
        button.config(text = curr_mark, state = DISABLED, disabledforeground = DIS_FONT, bg = DIS_BACK)
        self.sections[sec_num].incrCount()
        for i in range(9):
            for b in self.sections[i].getSection().winfo_children():
                if i != but_num and b["bg"] != WIN_COLOR:
                    b.config(state = DISABLED, bg = DIS_BACK)
                else:
                    if b["text"] == "":
                        b.config(state = NORMAL, bg = DEF_COLOR)
        if self.sections[but_num].getCount() >= 9:
            for i in range(9):
                for b in self.sections[i].getSection().winfo_children():
                    if b["text"] == "":
                        b.config(state = NORMAL, bg = DEF_COLOR)
        if not self.sections[sec_num].getWon():
            sec_win = self.checkSecWin(sec_num)
        if sec_win:
            self.checkGameWin()

    def checkSecWin(self, sec_num):
        WIN_COLOR = "red"
        section = self.sections[sec_num].getSection();
        if section.winfo_children()[0]["text"] != "":
            if section.winfo_children()[0]["text"] == section.winfo_children()[4]["text"] == section.winfo_children()[8]["text"]:
                self.sections[sec_num].setWinner(section.winfo_children()[0]["text"])
                section.winfo_children()[0].config(bg = WIN_COLOR)
                section.winfo_children()[4].config(bg = WIN_COLOR)
                section.winfo_children()[8].config(bg = WIN_COLOR)
                return 1
        for i in range(3):
            if section.winfo_children()[i]["text"] != "":
                if section.winfo_children()[i]["text"] == section.winfo_children()[i + 3]["text"] == section.winfo_children()[i + 6]["text"]:
                    self.sections[sec_num].setWinner(section.winfo_children()[i]["text"])
                    section.winfo_children()[i].config(bg = WIN_COLOR)
                    section.winfo_children()[i + 3].config(bg = WIN_COLOR)
                    section.winfo_children()[i + 6].config(bg = WIN_COLOR)
                    return 1
        for i in range(0, 9, 3):
            if section.winfo_children()[i]["text"] != "":
                if section.winfo_children()[i]["text"] == section.winfo_children()[i + 1]["text"] == section.winfo_children()[i + 2]["text"]:
                    self.sections[sec_num].setWinner(section.winfo_children()[i]["text"])
                    section.winfo_children()[i].config(bg = WIN_COLOR)
                    section.winfo_children()[i + 1].config(bg = WIN_COLOR)
                    section.winfo_children()[i + 2].config(bg = WIN_COLOR)
                    return 1
        if section.winfo_children()[2]["text"] != "":
            if section.winfo_children()[2]["text"] == section.winfo_children()[4]["text"] == section.winfo_children()[6]["text"]:
                self.sections[sec_num].setWinner(section.winfo_children()[2]["text"])
                section.winfo_children()[2].config(bg = WIN_COLOR)
                section.winfo_children()[4].config(bg = WIN_COLOR)
                section.winfo_children()[6].config(bg = WIN_COLOR)
                return 1
        return 0

    def checkGameWin(self):
        if self.sections[0].getWon():
            if self.sections[0].getWinner() == self.sections[4].getWinner() == self.sections[8].getWinner():
                self.winner(0)
                return
        for i in range(3):
            if self.sections[i].getWon():
                if self.sections[i].getWinner() == self.sections[i + 3].getWinner() == self.sections[i + 6].getWinner():
                    self.winner(i)
                    return
        for i in range(0, 9, 3):
            if self.sections[i].getWon():
                if self.sections[i].getWinner() == self.sections[i + 1].getWinner() == self.sections[i + 2].getWinner():
                    self.winner(i)
                    return
        if self.sections[2].getWon():
            if self.sections[2].getWinner() == self.sections[4].getWinner() == self.sections[6].getWinner():
                self.winner(2)
                return

    def winner(self, pos):
        winningMark = self.sections[pos].getWinner()
        if self.players[0].getMark() == winningMark:
            winningPlayer = self.players[0].getName()
            self.players[0].incrWins()
            self.players[0].incrStreak()
            self.players[1].resetStreak()
        else:
            winningPlayer = self.players[1].getName()
            self.players[1].incrWins()
            self.players[1].incrStreak()
            self.players[0].resetStreak()

        self.root.destroy()
        win_root = Tk()
        win_root.config(cursor = "target")
        bFont = Font(family = "Helvetica", size = 18)
        win_root.config(bg = self.COLOR)
        winFont = Font(family = "Helvetica", size = 60)
        subFontU = Font(family = "Helvetica", size = 25, underline = 1)
        subFont = Font(family = "Helvetica", size = 25)
        wCanvas = Canvas(win_root, height = self.MAIN_WIN_H, width = self.MAIN_WIN_W, bg = self.COLOR, highlightthickness = 0)
        wCanvas.create_text(self.MAIN_WIN_W / 2, 70, text = winningPlayer, font = winFont)
        wCanvas.create_text(self.MAIN_WIN_W / 2, 150, text = "WINS!!!", font = winFont)
        wCanvas.create_text(self.MAIN_WIN_W / 4, 210, text = self.players[0].getName(), font = subFontU)
        wCanvas.create_text(self.MAIN_WIN_W * (3 / 4), 210, text = self.players[1].getName(), font = subFontU)
        p1_text = self.players[0].getWins()
        if p1_text == 1:
            p1_text = str(p1_text) + " win"
        else:
            p1_text = str(p1_text) + " wins"
        p2_text = self.players[1].getWins()
        if p2_text == 1:
            p2_text = str(p2_text) + " win"
        else:
            p2_text = str(p2_text) + " wins"
        wCanvas.create_text(self.MAIN_WIN_W / 4, 250, text = p1_text, font = subFont)
        wCanvas.create_text(self.MAIN_WIN_W * (3 / 4), 250, text = p2_text, font = subFont)
        p2_streak = str(self.players[1].getStreak()) + " game streak"
        if self.players[0].getWins() > 0:
            p1_streak = str(self.players[0].getStreak()) + " game streak"
            wCanvas.create_text(self.MAIN_WIN_W / 4, 290, text = p1_streak, font = subFont)
        else:
            p2_streak = str(self.players[1].getStreak()) + " game streak"
            wCanvas.create_text(self.MAIN_WIN_W * (3 / 4), 290, text = p2_streak, font = subFont)
        wCanvas.pack()
        wFrame = Frame(win_root, bg = self.COLOR, height = 30)
        new_game = Button(wFrame, text = "New Game", font = bFont, command = lambda: self.game.processChoice(0, win_root, self.players))
        new_players = Button(wFrame, text = "New Players", font = bFont, command = lambda: self.game.processChoice(1, win_root, self.players))
        new_game.grid(row = 0, column = 0, padx = 50, pady = (0, 50))
        new_players.grid(row = 0, column = 1, padx = 50, pady = (0, 50))
        wFrame.pack(side = BOTTOM)
        win_root.mainloop()

    def getBoard(self):
        return self.board
