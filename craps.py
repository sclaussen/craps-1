import random

class Bankroll:
    money = 0

    def __init__(self, money):
        self.money = money


class Bet:
    PASS_LINE = 0
    PASS_LINE_ODDS = 1
    COME = 2
    POINT = 3
    POINT_ODDS = 4
    bets = {
        0 : "PASS_LINE",
        1 : "PASS_LINE_ODDS",
        2 : "COME",
        3 : "POINT",
        4 : "POINT_ODDS"
    }

    betType = -1
    money = 0
    point = 0

    def __init__(self, betType, money, point = 0):
        self.betType = betType
        self.money = money
        self.point = point

    def __str__(self):
        return "Bet: " + self.bets[self.betType] + " " + str(self.money) + " " + str(self.point)

class Dice:
    dice1 = 0
    dice2 = 0

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        return self.dice1 + self.dice2

    def __str__(self):
        return "Dice: " + str(self.dice1) + " " + str(self.dice2) + " " + str(self.dice1 + self.dice2)



bet = Bet(Bet.PASS_LINE, 5)
print(bet)

dice = Dice()
sum = dice.roll()
print(sum)
print(dice)
