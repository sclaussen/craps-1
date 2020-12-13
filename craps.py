import random

class Bankroll:
    money = 0

    def __init__(self, money):
        self.money = money
        print(self)


class Bet:
    PASS_LINE = 0
    COME = 1
    POINT = 2
    bets = {
        0 : "PASS_LINE",
        1 : "COME",
        2 : "POINT"
    }

    betType = -1
    oddsAmount = 0
    money = 0
    point = 0

    def __init__(self, betType, money, point = 0):
        self.betType = betType
        self.money = money
        self.point = point
        print(self)

    def addOdds(self, oddsAmount):
        self.oddsAmount = oddsAmount
        print(self)

    def setPoint(self, point):
        self.point = point
        print(self)

    def __str__(self):
        return "Bet: " + self.bets[self.betType] + " " + str(self.money) + " " + str(self.oddsAmount) + " " + str(self.point)


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



bet = Bet(Bet.PASS_LINE, 5)
bet.setPoint(6)
bet.addOdds(10)
print(bet)

# dice = Dice()
# sum = dice.roll()
# print(sum)
# print(dice)
