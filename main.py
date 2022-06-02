

import random

options = ['R', 'P', 'S']

def rock_paper_scissor():
    print('Rock - Paper - Scissors')
    print('R for Rock, P for Paper, S for Scissors')
    player_choice = input('Enter your choice: ')
    print('\n')

    while player_choice not in options:
        print('Invalid Choice')
        player_choice = input('Enter your choice: ')
        print('\n')

    player_choice = player_choice.upper()
    computer_choice = random.choice(options)

    print('Player Choice: ' + player_choice)
    print('Computer Choice: ' + computer_choice)
    print('\n')

    if player_choice == computer_choice:
        print('Tie!')
        rock_paper_scissor()

    elif player_choice == 'R' and computer_choice == 'S':
        print('You Win!')

    elif player_choice == 'P' and computer_choice == 'R':
        print ('You Win!')

    elif player_choice == 'S' and computer_choice == 'P':
        print ('You Win!')

    else:
        print('You Lose!')

rock_paper_scissor()        