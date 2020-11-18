class Player:
    def __init__(self, name):
        self.name = name
        self.mark = ""
        self.wins = 0
        self.streak = 0
        self.turn = 0
        self.p2 = None
        self.title = name + "'s turn"

    def getName(self):
        return self.name

    def turnName(self):
        return self.name + "'s Turn"

    def setMark(self, num):
        if num == 0:
            self.mark = "X"
            self.turn = 1
            self.p2.mark = "O"
            self.p2.turn = 0
        else:
            self.mark = "O"
            self.turn = 0
            self.p2.mark = "X"
            self.p2.turn = 1

    def setP2(self, p2):
        self.p2 = p2

    def getMark(self):
        return self.mark

    def getTurn(self):
        return self.turn

    def getWins(self):
        return self.wins

    def incrWins(self):
        self.wins += 1

    def getStreak(self):
        return self.streak

    def incrStreak(self):
        self.streak += 1

    def resetStreak(self):
        self.streak = 0

    def getTitle(self):
        return self.title

    def switchTurns(self):
        if self.turn == 0:
            self.turn = 1
            self.p2.turn = 0
        else:
            self.turn = 0
            self.p2.turn = 1
