# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:39:41 2022

@author: patry
"""

import random as rd

def intro():
    print('Welcome to ROLLING DICE!')
    amount_of_dices()
    
def random_number():
    return rd.randint(1,6)

def showing_dice(number):
    pass
    
def amount_of_dices():
    while True:
        try:
            answer = int(input('Choose an amount of dices to roll: '))
            if answer > 0:
                rolling_dice(answer)
                break
            else:
                1/0
        except ValueError:
            print('Amount must be an integer. Try again.')
            continue
        except ZeroDivisionError:
            print('Amount must be higher than 0. Try again.')
            continue
    again(answer)

def rolling_dice(amount):
    numbers = []
    for i in range(amount):
        rand_number = random_number()
        print('{}. dice: {}'.format(i+1,rand_number))
        # print('{}. dice: {}'.format(i+1,showing_dice(rand_number)))
        numbers.append(rand_number)
    if amount > 1:
        print('Sum of numbers: {}'.format(sum(numbers)))

def again(amount):
    while True:
        try:
            answer = str(input('''Type \'enter\' to continue or
type a number to change an amount of dices or
type '0' to escape.: '''))
            if answer == '':
                print('')
                rolling_dice(amount)
                again(amount)
                break
            elif int(answer) > 0:
                print('')
                rolling_dice(int(answer))
                again(int(answer))
                break
            elif answer == '0':
                input('Good bye!')
                break
            else:
                1/0
        except ValueError or ZeroDivisionError:
            print('\nWrong value. Try again.')
            continue    

intro()