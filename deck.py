from card import Card

ranks = [x for x in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['DIAMONDS', 'SPADES', 'HEARTS', 'CLUBS']

class Deck:
    
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def deal(self):
        return self.cards.pop()

    def clear(self):
        self.cards.clear()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += f'\n{card}'
        return deck_string