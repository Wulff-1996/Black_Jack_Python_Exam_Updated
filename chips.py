class Chips:

    def __init__(self, money):
        self.money = money
        self.bet = 0

    def win_bet(self):
        self.money += 2*self.bet

    def win_tie(self):
        self.money += self.bet

    def __str__(self):
        return f'money: {self.money}, bet: {self.bet}'