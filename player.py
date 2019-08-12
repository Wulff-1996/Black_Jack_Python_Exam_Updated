from hand import Hand
from chips import Chips

class Player:
    PLAYER = 'PLAYER'
    DEALER = 'DEALER'
    YOU = 'YOU'
    COMPUTER = 'COMPUTER'

    def __init__(self, role: str, hand: Hand, chips: Chips, name: str):
        self.chips = chips
        self.hand = hand
        self.role = role
        self.name = name 