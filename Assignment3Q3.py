'''
Ahmad Alqattan
2192131011
Homework 3
Question 3
'''

import random

comNum = random.randint(1,3)
userNum = int(input('Enter 1 for rock, 2 for paper, 3 for scissors: '))

while True:
    userChoice = ''
    comChoice = ''
    if userNum == 1:
        userChoice = 'rock'
    elif userNum == 2:
        userChoice = 'paper'
    else:
        userChoice = 'scissors'

    if comNum == 1:
        comChoice = 'rock'
    elif comNum == 2:
        comChoice = 'paper'
    else:
        comChoice = 'scissors'
    print(f'Computer chose {comChoice}')
    print(f'You chose {userChoice}')
    if userNum == comNum:
        print('You made the same choice as the computer. Starting over')
    else:
        if (userNum == 1 and comNum == 3) or (userNum == 2 and comNum == 1) or (userNum == 3 and comNum == 2):
            print('You win the game')
        else:
            print('You lost the game')
        break
    comNum = random.randint(1, 3)
    userNum = int(input('Enter 1 for rock, 2 for paper, 3 for scissors: '))

