from tkinter import *
from tkinter.font import *
import random

MAIN_WIN_W = 500
MAIN_WIN_H = 350
GAME_WIN_W = 500
GAME_WIN_H = 650
COLOR = "SteelBlue3"
DIS_BACK = "gray70"
DIS_FONT = "black"
DEF_COLOR = "gray90"

global game_root
global mFont
global players
global curr_player
global sections
global tCanvas
global curr_mark
global count
global game_squares

def main():
    curr_section = None
    root = Tk()
    mainFont = Font(family = "Helvetica", size = 36)
    secFont = Font(family = "Helvetica", size = 20)
    bFont = Font(family = "Helvetica", size = 18)
    canvas = Canvas(root, width = MAIN_WIN_W, height = MAIN_WIN_H, bg = COLOR)
    canvas.create_text(MAIN_WIN_W / 2, 50, text = "MEGA TIC TAC TOE", font = mainFont)
    canvas.create_text(MAIN_WIN_W / 2, 120, text = "Player's Names", font = mainFont)
    canvas.create_text(MAIN_WIN_W / 5, 200, text = "Player 1:", font = secFont)
    canvas.create_text(MAIN_WIN_W / 5, 240, text = "Player 2:", font = secFont)
    p1 = Entry(canvas)
    p1.place(x = 160, y = 200, width = 295, height = 25, anchor = W)
    p2 = Entry(canvas)
    p2.place(x = 160, y = 240, width = 295, height = 25, anchor = W)
    submit = Button(canvas, text = "Start Game", font = bFont, command = lambda: playerSetup(root, p1, p2))
    submit.place(x = MAIN_WIN_W / 2, y = 303, anchor = CENTER)
    canvas.grid()

    root.mainloop()

def playerSetup(root, p1, p2):
    global players
    players = [p1.get().title(), p2.get().title()]
    temp = []
    for player in players:
        if player.endswith("s"):
            player += "' Turn"
        else:
            player += "'s Turn"
        temp.append(player)
    players = temp
    root.destroy()
    startGame()

def startGame():
    global players
    global game_root
    global curr_player
    global tCanvas
    global sections
    global curr_mark
    global count
    global game_squares
    game_root = Tk()
    bFont = Font(family = "Helvetica", size = 18)
    game_root.config(bg = COLOR)
    game_root.geometry(str(GAME_WIN_W) + "x" + str(GAME_WIN_H))
    mFont = Font(family = "Helvetica", size = 36)
    r = random.randint(0, 1)
    game_squares = ["", "", "", "", "", "", "", "", ""]

    curr_player = players[r]
    curr_mark = "O"
    tCanvas = Canvas(game_root, width = GAME_WIN_W, height = 80, bg = COLOR, highlightthickness = 0)
    tCanvas.create_text(GAME_WIN_W / 2, 40, text = curr_player, font = mFont)

    middle = Frame(game_root)
    sections = createGrid(middle)
    count = [0,0,0,0,0,0,0,0,0]

    bottom = Frame(game_root, bg = COLOR)
    restart = Button(bottom, text = "Start Over", font = bFont, command = lambda: restartProcess())
    restart.grid(pady = 25)

    tCanvas.pack()
    middle.pack()
    bottom.pack()
    runGame()

def restartProcess():
    game_root.destroy()
    startGame()

def runGame():
    global curr_player
    global curr_mark
    mFont = Font(family = "Helvetica", size = 36)
    if curr_player == players[0]:
        curr_player = players[1]
    else:
        curr_player = players[0]
    if curr_mark == "X":
        curr_mark = "O"
    else:
        curr_mark = "X"
    tCanvas.delete("all")
    tCanvas.create_text(GAME_WIN_W / 2, 40, text = curr_player, font = mFont)

def process(b_num, sec_num, button):
    global count
    mark_font = Font(family = "Helvetica", size = 80)
    sec_win = ""
    count[sec_num] += 1
    button.config(text = curr_mark, state = DISABLED, disabledforeground = DIS_FONT, bg = DIS_BACK)
    sec_win = checkSecWin(sec_num)
    checkGameWin()
    if sec_win != "":
        if sec_win == "X":
            xCanvas = Canvas(sections[sec_num], width = 134, height = 146)
            xCanvas.create_text(67, 73, text = "X", font = mark_font)
            xCanvas.grid(row = 0, column = 0, rowspan = 4, columnspan = 4)
            sections[sec_num].lift(xCanvas)
        if sec_win == "O":
            xCanvas = Canvas(sections[sec_num], width = 134, height = 146)
            xCanvas.create_text(67, 73, text = "O", font = mark_font)
            xCanvas.grid(row = 0, column = 0, rowspan = 4, columnspan = 4)
            sections[sec_num].lift(xCanvas)
    for i in range(9):
        for b in sections[i].winfo_children():
            if isinstance(b, Button):
                if i != b_num:
                    b.config(state = DISABLED, bg = DIS_BACK)
                else:
                    if b["text"] == "":
                        b.config(state = NORMAL, bg = DEF_COLOR)
            elif isinstance(b, Canvas):
                count[i] = 10
    if count[b_num] >= 9:
        for i in range(9):
            for b in sections[i].winfo_children():
                if isinstance(b, Button):
                    if b["text"] == "":
                        b.config(state = NORMAL, bg = DEF_COLOR)
    runGame()

def checkSecWin(sec_num):
    section = sections[sec_num]
    if section.winfo_children()[0]["text"] != "":
        if section.winfo_children()[0]["text"] == section.winfo_children()[4]["text"] == section.winfo_children()[8]["text"]:
            game_squares[sec_num] = section.winfo_children()[0]["text"]
            return section.winfo_children()[0]["text"]
    for i in range(3):
        if section.winfo_children()[i]["text"] != "":
            if section.winfo_children()[i]["text"] == section.winfo_children()[i + 3]["text"] == section.winfo_children()[i + 6]["text"]:
                game_squares[sec_num] = section.winfo_children()[i]["text"]
                return section.winfo_children()[i]["text"]
    for i in range(0, 9, 3):
        if section.winfo_children()[i]["text"] != "":
            if section.winfo_children()[i]["text"] == section.winfo_children()[i + 1]["text"] == section.winfo_children()[i + 2]["text"]:
                game_squares[sec_num] = section.winfo_children()[i]["text"]
                return section.winfo_children()[i]["text"]
    if section.winfo_children()[2]["text"] != "":
        if section.winfo_children()[2]["text"] == section.winfo_children()[4]["text"] == section.winfo_children()[6]["text"]:
            game_squares[sec_num] = section.winfo_children()[2]["text"]
            return section.winfo_children()[2]["text"]
    return ""

def checkGameWin():
    if game_squares[0] != "":
        if game_squares[0] == game_squares[4] == game_squares[8]:
            winner(curr_player)
            return
    for i in range(3):
        if game_squares[i] != "":
            if game_squares[i] == game_squares[i + 3] == game_squares[i + 6]:
                winner(curr_player)
                return
    for i in range(0, 9, 3):
        if game_squares[i] != "":
            if game_squares[i] == game_squares[i + 1] == game_squares[i + 2]:
                winner(curr_player)
                return
    if game_squares[2] != "":
        if game_squares[2] == game_squares[4] == game_squares[6]:
            winner(curr_player)
            return

def winner(player):
    game_root.destroy()
    win_root = Tk()
    bFont = Font(family = "Helvetica", size = 18)
    win_root.config(bg = COLOR)
    winFont = Font(family = "Helvetica", size = 60)
    player = player.split("'")[0].upper()
    wCanvas = Canvas(win_root, height = MAIN_WIN_H, width = MAIN_WIN_W, bg = COLOR, highlightthickness = 0)
    wCanvas.create_text(MAIN_WIN_W / 2, 117, text = player, font = winFont)
    wCanvas.create_text(MAIN_WIN_W / 2, 234, text = "WINS!!!", font = winFont)
    wCanvas.pack()
    wFrame = Frame(win_root, bg = COLOR, height = 30)
    new_game = Button(wFrame, text = "New Game", font = bFont, command = lambda: processChoice(0, win_root))
    new_players = Button(wFrame, text = "New Players", font = bFont, command = lambda: processChoice(1, win_root))
    new_game.grid(row = 0, column = 0, padx = 50, pady = (0, 50))
    new_players.grid(row = 0, column = 1, padx = 50, pady = (0, 50))
    wFrame.pack(side = BOTTOM)
    win_root.mainloop()

def processChoice(choice, root):
    root.destroy()
    if choice == 0:
        startGame()
    else:
        main()

def createGrid(middle):
    frame_relief = "solid"
    bd = 3
    button_overrelief = "groove"
    font = 20
    h = 2
    w = 4

    ul = Frame(middle, relief = frame_relief, bd = bd)
    ul.grid(row = 0, column = 0)

    ulb1 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 0, ulb1))
    ulb1.grid(row = 0, column = 0)
    ulb2 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 0, ulb2))
    ulb2.grid(row = 0, column = 1)
    ulb3 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 0, ulb3))
    ulb3.grid(row = 0, column = 2)
    ulb4 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 0, ulb4))
    ulb4.grid(row = 1, column = 0)
    ulb5 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 0, ulb5))
    ulb5.grid(row = 1, column = 1)
    ulb6 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 0, ulb6))
    ulb6.grid(row = 1, column = 2)
    ulb7 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 0, ulb7))
    ulb7.grid(row = 2, column = 0)
    ulb8 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 0, ulb8))
    ulb8.grid(row = 2, column = 1)
    ulb9 = Button(ul, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 0, ulb9))
    ulb9.grid(row = 2, column = 2)

    um = Frame(middle, relief = frame_relief, bd = bd)
    um.grid(row = 0, column = 1)

    umb1 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 1, umb1))
    umb1.grid(row = 0, column = 0)
    umb2 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 1, umb2))
    umb2.grid(row = 0, column = 1)
    umb3 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 1, umb3))
    umb3.grid(row = 0, column = 2)
    umb4 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 1, umb4))
    umb4.grid(row = 1, column = 0)
    umb5 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 1, umb5))
    umb5.grid(row = 1, column = 1)
    umb6 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 1, umb6))
    umb6.grid(row = 1, column = 2)
    umb7 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 1, umb7))
    umb7.grid(row = 2, column = 0)
    umb8 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 1, umb8))
    umb8.grid(row = 2, column = 1)
    umb9 = Button(um, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 1, umb9))
    umb9.grid(row = 2, column = 2)

    ur = Frame(middle, relief = frame_relief, bd = bd)
    ur.grid(row = 0, column = 2)

    urb1 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 2, urb1))
    urb1.grid(row = 0, column = 0)
    urb2 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 2, urb2))
    urb2.grid(row = 0, column = 1)
    urb3 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 2, urb3))
    urb3.grid(row = 0, column = 2)
    urb4 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 2, urb4))
    urb4.grid(row = 1, column = 0)
    urb5 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 2, urb5))
    urb5.grid(row = 1, column = 1)
    urb6 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 2, urb6))
    urb6.grid(row = 1, column = 2)
    urb7 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 2, urb7))
    urb7.grid(row = 2, column = 0)
    urb8 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 2, urb8))
    urb8.grid(row = 2, column = 1)
    urb9 = Button(ur, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 2, urb9))
    urb9.grid(row = 2, column = 2)

    ml = Frame(middle, relief = frame_relief, bd = bd)
    ml.grid(row = 1, column = 0)

    mlb1 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 3, mlb1))
    mlb1.grid(row = 0, column = 0)
    mlb2 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 3, mlb2))
    mlb2.grid(row = 0, column = 1)
    mlb3 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 3, mlb3))
    mlb3.grid(row = 0, column = 2)
    mlb4 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 3, mlb4))
    mlb4.grid(row = 1, column = 0)
    mlb5 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 3, mlb5))
    mlb5.grid(row = 1, column = 1)
    mlb6 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 3, mlb6))
    mlb6.grid(row = 1, column = 2)
    mlb7 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 3, mlb7))
    mlb7.grid(row = 2, column = 0)
    mlb8 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 3, mlb8))
    mlb8.grid(row = 2, column = 1)
    mlb9 = Button(ml, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 3, mlb9))
    mlb9.grid(row = 2, column = 2)

    mm = Frame(middle, relief = frame_relief, bd = bd)
    mm.grid(row = 1, column = 1)

    mmb1 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 4, mmb1))
    mmb1.grid(row = 0, column = 0)
    mmb2 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 4, mmb2))
    mmb2.grid(row = 0, column = 1)
    mmb3 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 4, mmb3))
    mmb3.grid(row = 0, column = 2)
    mmb4 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 4, mmb4))
    mmb4.grid(row = 1, column = 0)
    mmb5 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 4, mmb5))
    mmb5.grid(row = 1, column = 1)
    mmb6 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 4, mmb6))
    mmb6.grid(row = 1, column = 2)
    mmb7 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 4, mmb7))
    mmb7.grid(row = 2, column = 0)
    mmb8 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 4, mmb8))
    mmb8.grid(row = 2, column = 1)
    mmb9 = Button(mm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 4, mmb9))
    mmb9.grid(row = 2, column = 2)

    mr = Frame(middle, relief = frame_relief, bd = bd)
    mr.grid(row = 1, column = 2)

    mrb1 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 5, mrb1))
    mrb1.grid(row = 0, column = 0)
    mrb2 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 5, mrb2))
    mrb2.grid(row = 0, column = 1)
    mrb3 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 5, mrb3))
    mrb3.grid(row = 0, column = 2)
    mrb4 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 5, mrb4))
    mrb4.grid(row = 1, column = 0)
    mrb5 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 5, mrb5))
    mrb5.grid(row = 1, column = 1)
    mrb6 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 5, mrb6))
    mrb6.grid(row = 1, column = 2)
    mrb7 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 5, mrb7))
    mrb7.grid(row = 2, column = 0)
    mrb8 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 5, mrb8))
    mrb8.grid(row = 2, column = 1)
    mrb9 = Button(mr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 5, mrb9))
    mrb9.grid(row = 2, column = 2)

    ll = Frame(middle, relief = frame_relief, bd = bd)
    ll.grid(row = 2, column = 0)

    llb1 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 6, llb1))
    llb1.grid(row = 0, column = 0)
    llb2 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 6, llb2))
    llb2.grid(row = 0, column = 1)
    llb3 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 6, llb3))
    llb3.grid(row = 0, column = 2)
    llb4 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 6, llb4))
    llb4.grid(row = 1, column = 0)
    llb5 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 6, llb5))
    llb5.grid(row = 1, column = 1)
    llb6 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 6, llb6))
    llb6.grid(row = 1, column = 2)
    llb7 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 6, llb7))
    llb7.grid(row = 2, column = 0)
    llb8 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 6, llb8))
    llb8.grid(row = 2, column = 1)
    llb9 = Button(ll, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 6, llb9))
    llb9.grid(row = 2, column = 2)

    lm = Frame(middle, relief = frame_relief, bd = bd)
    lm.grid(row = 2, column = 1)

    lmb1 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 7, lmb1))
    lmb1.grid(row = 0, column = 0)
    lmb2 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 7, lmb2))
    lmb2.grid(row = 0, column = 1)
    lmb3 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 7, lmb3))
    lmb3.grid(row = 0, column = 2)
    lmb4 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 7, lmb4))
    lmb4.grid(row = 1, column = 0)
    lmb5 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 7, lmb5))
    lmb5.grid(row = 1, column = 1)
    lmb6 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 7, lmb6))
    lmb6.grid(row = 1, column = 2)
    lmb7 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 7, lmb7))
    lmb7.grid(row = 2, column = 0)
    lmb8 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 7, lmb8))
    lmb8.grid(row = 2, column = 1)
    lmb9 = Button(lm, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 7, lmb9))
    lmb9.grid(row = 2, column = 2)

    lr = Frame(middle, relief = frame_relief, bd = bd)
    lr.grid(row = 2, column = 2)

    lrb1 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(0, 8, lrb1))
    lrb1.grid(row = 0, column = 0)
    lrb2 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(1, 8, lrb2))
    lrb2.grid(row = 0, column = 1)
    lrb3 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(2, 8, lrb3))
    lrb3.grid(row = 0, column = 2)
    lrb4 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(3, 8, lrb4))
    lrb4.grid(row = 1, column = 0)
    lrb5 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(4, 8, lrb5))
    lrb5.grid(row = 1, column = 1)
    lrb6 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(5, 8, lrb6))
    lrb6.grid(row = 1, column = 2)
    lrb7 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(6, 8, lrb7))
    lrb7.grid(row = 2, column = 0)
    lrb8 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(7, 8, lrb8))
    lrb8.grid(row = 2, column = 1)
    lrb9 = Button(lr, overrelief = button_overrelief, font = font, height = h, width = w, command = lambda: process(8, 8, lrb9))
    lrb9.grid(row = 2, column = 2)

    sections = [ul, um, ur, ml, mm, mr, ll, lm, lr]
    return sections

main()
