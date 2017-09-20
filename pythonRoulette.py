'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

import random


bank_account = 1000
bet_amount = 0
bet_color = "red"
bet_number = 0
ball = 0

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
# odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
# even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]

def take_bet():
    bet_amount = input("Enter bet amount: ")
    while bet_amount > bank_account:
        print("Insufficient funds")
        bet_amount = input("Enter bet amount: ")
    bet_color = str(input("Enter bet color: "))
    bet_number = input("Enter bet number: ")
    roll_ball(bet_number,bet_amount)

def roll_ball(bet_number,bet_amount):
    ball = random.randint(1,37)
    check_results(ball,bet_number,bet_amount,bank_account)

    '''returns a random number between 0 and 37'''

def check_results(ball,bet_number,bet_amount,bank_account):
    if ball == bet_number:
        bank_account = bank_account + bet_amount
        print("winner")
        play_game()
    else:
        print("fucking loser")
        bank_account = bank_account - bet_amount
        play_game()
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''



def payout():
    '''returns total amount won or lost by user based on results of roll. '''
    pass

def play_game():
    take_bet()
    print(bank_account)
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:

    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """


play_game()

