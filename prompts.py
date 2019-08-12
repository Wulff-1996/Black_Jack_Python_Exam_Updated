from chips import Chips
from player import Player
from hand import Hand
from deck import Deck
import sys

def promt_player_dealer():
    while True:
        print('Do you want to be the player or the dealer? \n   -let me be the dealer, love to take all your money ;)\n   -then I would buy some new proccessors.. \n1: player \n2: dealer')
        try:
            player_role_data = int(input())
        except ValueError:
            print('input must be an integer\n  -...oh sorry means a natural number.., forgot you are so stupid, you pinhead.')
        else:
            if player_role_data == 1:
                return Player.PLAYER
                break
            elif player_role_data == 2:
                return Player.DEALER
                break
            else:
                print('INVALID INPUT!!, stupid simpleton you are.., only integer values are valid...')

def promt_money_amount():
    while True:
        print('Enter the players money \n  -dont be gready ;)')
        try:
            player_money = int(input())
        except ValueError:
            print('input must be an integer')
        else:
            if player_money <= 0:
                print('You cannot deposit a number that is zero or lower. \n-no wonder you have no money, ahah..')
            else:
                return player_money
                break

def take_bet(chips: Chips):
    while True:
        print(f'Place bet, you have {chips.money} avaliable:')
        try:
            chips.bet = int(input())
        except ValueError:
            print('INVALID INPUT, must be a number... \nyou imbecile muttonhead..')
        else:
            if chips.bet <= 0:
                print(f'INVALID, number must be over zero. \n-???... errr.. no words.. oh wait, ..you moron.')
            elif chips.bet > chips.money:
                print(f'You cannot bet {chips.bet}, when you only have {chips.money} avaliable. \n-did you even graduated kindergarden!! haha, you bonehead')
            else:
                chips.money -= chips.bet
                break

def prompt_hit_stand(hand: Hand, deck: Deck, func):
    while True:
        print('Do you want to take another card? \n -com on, dont be a chicken! \n1: Hit \n2: Stand')
        try:
            will_player_hit = int(input())
        except ValueError:
            print('INVALID INPUT, must be a number... stupid stupid stupid you...')
        else:
            if will_player_hit == 1:
                func(hand, deck)
                break
            elif will_player_hit == 2:
                print('You stay, dealer is now playing, prey for the best, haha :)')
                return False
                break
            else:
                print('invalid number\n -there is only two options, you are a lost course, you nitwit..')

def prompt_new_game():
    while True:
        print('Round over. \n2: new game \n9: quit')
        try:
            will_play_again_data = int(input())
        except ValueError:
            print('INVALID INPUT!!, stupid jerk you are.., only integer values are valid...')
        else:
            if will_play_again_data == 2:
                return False
                break
            elif will_play_again_data == 9:
                sys.exit('Player exited the game')
                break
            else:
                print('INVALID INPUT!!, OMG you are stupid, just quit the game you twit!!!\nenter a valid number..')

def promt_to_contionue():
    while True:
        print('Round over. \n1: continue \n2: new game \n9: quit')
        try:
            will_continue_data = int(input())
        except ValueError:
            print('input must be an integer \n  -..GOD you are stupid, just like a bonehead, oh wait you are haha, Im so funny.')
        else:
            if will_continue_data == 1:
                return True 
                break
            elif will_continue_data == 2:
                return False
                break
            elif will_continue_data == 9:
                sys.exit('The player was so stupid that he/she/it exited the game\n -we have a word for that kind, .. CHICKEN!!')
                break
            else:
                print('INVALID INPUT, enter a valid input\n -yes a number you know... ???, like 1, 2 or 9, you moron!.')

def prompt_user_to_continue():
    print('smash the keyboard to proceed\n  -I know you like to punch things!..')
    input()