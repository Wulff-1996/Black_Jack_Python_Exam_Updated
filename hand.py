class Hand:
    
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        hand_string = 'hand: '
        for card in self.cards:
            hand_string += f'{card}, '
        return hand_string