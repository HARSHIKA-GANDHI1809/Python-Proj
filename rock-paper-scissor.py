import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {
    ROCK: '🪨',
    PAPER: '📜',
    SCISSORS: '✂️'
}

choices = tuple(emojis.keys())


def get_user_choice():

    while True:

        user_choice = input('Rock, paper, scissor? (r/p/s): ').lower()

        if user_choice in choices:
            return user_choice

        else:
            print('Invalid Choice!')


def display_choices(user_choice, ai_choice):

    print(f'You chose {emojis[user_choice]}')
    print(f'AI chose {emojis[ai_choice]}')


def determine_winner(user_choice, ai_choice):

    if user_choice == ai_choice:
        print('TIE!')

    elif (
        (user_choice == ROCK and ai_choice == SCISSORS) or
        (user_choice == SCISSORS and ai_choice == PAPER) or
        (user_choice == PAPER and ai_choice == ROCK)
    ):
        print('You Win 🎊')

    else:
        print('You Lose 🫠')


def play_game():

    while True:

        user_choice = get_user_choice()

        ai_choice = random.choice(choices)

        display_choices(user_choice, ai_choice)

        determine_winner(user_choice, ai_choice)

        should_cont = input('Continue? (y/n): ').lower()

        if should_cont == 'n':
            break


play_game()
