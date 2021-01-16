import random


class Bankroll:
    amount = 0

    def __init__(self, amount):
        self.amount = amount
        print(self)

    def withdraw(self, amount):
        self.amount -= amount
        return amount

    def __str__(self):
        s = "Bankroll:"
        s += "  " + str(self.amount)
        return s

class Bet:
    PASS_LINE = "Pass Line Bet"
    COME = "Come Bet"
    POINT = "Point Bet"
    type = -1
    odds = 0
    base = 0
    point = 0

    def __init__(self, type, base, point = 0):
        self.type = type
        self.base = base
        self.point = point
        print(self)

    def addOdds(self, odds):
        self.odds = odds
        print(self)

    def setPoint(self, point):
        self.point = point
        print(self)

    def __str__(self):
        s = "Bet:"
        s += "  " + str(self.type)
        s += "  " + str(self.odds)
        s += "  " + str(self.base)
        s += "  " + str(self.point)
        return s


class Dice:
    dice1 = 0
    dice2 = 0

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        print(self)
        return self.dice1 + self.dice2

    def __str__(self):
        return "Dice: " + str(self.dice1) + " " + str(self.dice2) + " " + str(self.dice1 + self.dice2)


def controller():
    bankroll = Bankroll(1000)
    for _ in range(4):
        bet = Bet(Bet.PASS_LINE, bankroll.withdraw(5))


controller()
