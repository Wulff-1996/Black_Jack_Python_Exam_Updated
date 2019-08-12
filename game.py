import random
import os
import sys
from chips import Chips
from card import Card
from deck import Deck
from hand import Hand
from player import Player
from prompts import promt_player_dealer, promt_money_amount, take_bet, prompt_hit_stand, prompt_new_game, promt_to_contionue, prompt_user_to_continue

################### functions  ##########################################
def computer_take_bet(chips: Chips):
    if chips.money >= 100:
        chips.bet = 50
        chips.money -= 50
    elif chips.money >= 50 < 100:
        chips.bet = 25
        chips.money -= 25
    elif chips.money > 10 < 50:
        chips.bet = 5
        chips.money -= 5
    else:
        chips.bet = 1
        chips.money -= 1

def calculate_hand(cards):
        total = 0
        aces = 0
        for card in cards:
            if card.rank in range(2, 11):
                total += card.rank
            elif card.rank == 'ACE':
                total += 11
                aces += 1
            else:
                total += 10
        if total > 21 and aces > 0:
            for ace in range(aces):
                if total > 21:
                    total -= 10
        return total

def hit(hand: Hand, deck: Deck):
    hand.add_card(deck.deal())
    calculate_hand(hand.cards)

def calcultate_one_card(card):
    if card.rank in range(2, 11):
        return card.rank
    elif card.rank == 'ACE':
        return 11
    else:
        return 10

################# functions for handle end of game #####################################
def you_lost(role, player: Player):
    print('---YOU LOST---')

    if role == Player.DEALER:
        print(f'    -you lost {player.chips.bet} to the computer\n    -now I will unfriend you on facebook, hate loosers!')
        player.chips.win_bet()
    else:
        print(f'    -you lost {player.chips.bet}\n    -now you are scewed, what will you tell your fiends?\n    -I forgot.. you dont have any haha, looser!!')

def you_won(role, player: Player):
    print('---YOU WON---')

    if role == Player.PLAYER:
        print(f'    -won {player.chips.bet}\n   -now you pay me a beer!, so thirsty of all that computer processing:)')
        player.chips.win_bet()
    else:
        print(f'    -you made the player loose {player.chips.bet}\n    -that was the money he would have bought food for his children\n    -you have no heart... Just like me yeah!! :)')


def tie(role, player: Player):
    print('---TIE---')

    if role == Player.PLAYER:
        print(f'    -you won {player.chips.bet} back\n   -you know that you have to win right?.. you Bonehead :|')
    else:
        print('    -the computer won its {player.chips.bet}\n   -dont let the computer take all your money, you bastard..')
    player.chips.win_tie()

################# functions for display in the terminal  ####################################
def show_cards(player: Player, dealer, is_dealer_hidden: bool):
    print( '-------------------------------------------------------------------------------')
    print(f'|{player.name}: {player.role}')
    print(f'|   money: {player.chips.money}')
    print(f'|   bet: {player.chips.bet}')
    print( '|   total: ' + str(calculate_hand(player.hand.cards)))
    print( '|   players hand: ' + str([str(card) for card in player.hand.cards]))
    print( '|')
    print(f'|{dealer.name}: {dealer.role}')
    if is_dealer_hidden:
        print('|    total: ' + str(calcultate_one_card(dealer.hand.cards[1])))
        print('|    dealers hand: <HIDDEN CARD>, ' + str(dealer.hand.cards[1]))
    else:
        print('|    total: ' + str(calculate_hand(dealer.hand.cards)))
        print('|    dealers hand: ' + str([str(card) for card in dealer.hand.cards]))
    print( '-------------------------------------------------------------------------------')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_terminal_show_cards(player: Player, dealer, is_dealer_hidden):
    clear_terminal()
    show_cards(player, dealer, is_dealer_hidden)


def play():
    # the game
    # flags for game states
    is_playing = True
    is_continue = True
    is_drawing_card = True

    while is_playing:
        # reset them to true if they were false and started a new game
        is_continue = True
        is_drawing_card = True
        clear_terminal()

        # get if the user is a player or a dealer
        role = promt_player_dealer()
        clear_terminal()

        # get the players money
        money = promt_money_amount()
        clear_terminal()

        # create the playeres with an empty hand
        if role == Player.PLAYER:
            player = Player(Player.PLAYER, Hand(), Chips(money), Player.YOU)
            dealer = Player(Player.DEALER, Hand(), Chips(0), Player.COMPUTER)
        else:
            player = Player(Player.PLAYER, Hand(), Chips(money), Player.COMPUTER)
            dealer = Player(Player.DEALER, Hand(), Chips(0), Player.YOU)

        # play round while, player money > 0
        while is_continue:
            is_drawing_card = True

            # create a deck and shuffle the deck
            deck = Deck()
            random.shuffle(deck.cards)

            # get bet for the player
            if role == player.PLAYER:
                clear_terminal()
                take_bet(player.chips)
            else:
                clear_terminal()
                computer_take_bet(player.chips)

            # clear the hands if they already placed a round
            player.hand = Hand()
            dealer.hand = Hand()

            # deal starting hand
            player.hand.add_card(deck.deal())
            player.hand.add_card(deck.deal())
            dealer.hand.add_card(deck.deal())
            dealer.hand.add_card(deck.deal())

            # game logic for when the user is the player
            if role == player.PLAYER:

                # show starting hand
                clear_terminal_show_cards(player, dealer, True)

                # deal cards until the player stops
                while is_drawing_card == True and calculate_hand(player.hand.cards) < 21:
                    is_drawing_card = prompt_hit_stand(player.hand, deck, hit)
                    clear_terminal_show_cards(player, dealer, True)
                
                # if drawing was cancelled by 21 set it to false
                is_drawing_card = False
                
                # calculate totals for player
                player_total = calculate_hand(player.hand.cards)

                # see if the player lost or if the dealer have to draw cards
                if player_total > 21:
                    you_lost(role, player)
                else:
                    # show dealers card
                    clear_terminal_show_cards(player, dealer, False)

                    # dealers turn
                    while calculate_hand(dealer.hand.cards) < 17:
                        hit(dealer.hand, deck)
                        clear_terminal_show_cards(player, dealer, False)
                    
                    dealer_total = calculate_hand(dealer.hand.cards)

                    # calculate who wins
                    if dealer_total > 21:
                        you_won(role, player)
                    elif dealer_total < player_total:
                        you_won(role, player)
                    elif dealer_total == player_total:
                        tie(role, player)
                    else:
                        you_lost(role, player)
            
            # game when user is the dealer           
            else:
                dealer_total = calcultate_one_card(dealer.hand.cards[1])
                
                # logic for computer to hit
                computer_is_playing = True
                while computer_is_playing:
                    clear_terminal_show_cards(player, dealer, True)
                    prompt_user_to_continue()

                    player_total = calculate_hand(player.hand.cards)
                    if player_total <= 11:
                        hit(player.hand, deck)
                    elif dealer_total >= 10 and player_total <= 17:
                        hit(player.hand, deck)
                    elif dealer_total < 10 and player_total <= 15:
                        hit(player.hand, deck)
                    else:
                        break

                # calculate totals for player
                player_total = calculate_hand(player.hand.cards)

                # see if the player lost or the dealer have to play
                if player_total > 21:
                    you_won(role, player)
                else:
                    clear_terminal_show_cards(player, dealer, False)
                    prompt_user_to_continue()

                    # dealers turn
                    while calculate_hand(dealer.hand.cards) < 17:
                        hit(dealer.hand, deck)
                        clear_terminal_show_cards(player, dealer, False)
                        prompt_user_to_continue()
                    
                    dealer_total = calculate_hand(dealer.hand.cards)

                    if dealer_total > 21:
                        you_lost(role, player)
                    elif dealer_total < player_total:
                        you_lost(role, player)
                    elif dealer_total == player_total:
                        tie(role, player)
                    else:
                        you_won(role, player)

            # promt for continue, new game or quit
            if player.chips.money <= 0:
                is_continue = False
                is_continue = prompt_new_game()
            else:
                is_continue = promt_to_contionue()


if __name__ == "__main__":
    play()