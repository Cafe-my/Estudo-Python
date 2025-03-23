print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses

 
from random import choice                   # comando choice do modulo random -> permite sortear um elemento aleatorio dentro de uma sequencia (lista, tuplas, set)
the_num = choice([1,2,3,4,5,6,7,8,9,10])

guess = int(input('Guess a number between 1 and 10. You have 3 attempts: '))
if guess == the_num:
    print('Congratulations, your guess is correct!')
else:
    i = 1
    while guess != the_num:
        guess = int(input("It's incorrect! Try again: "))
        i += 1
        if guess == the_num:
            print('Congratulations, your guess is correct!')
        elif i == 3 and guess != the_num:    
            print("Your attempts is over!")
            break
print(f"The correct number is {the_num}!")


# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.

from random import randint      # comando randint do modulo random, permite retornar um número inteiro aleatório entre um determinado intervalo.
the_num = randint(1,100)

guess = int(input('Guess a number between 1 and 100. You have 10 attempts: '))

if guess == the_num:
    print('Congratulations, your guess is correct!')
else:
    i = 1
    while guess != the_num:
        if guess < the_num:
            print("The guess is too low!")
        elif guess > the_num:
            print("The guess is too high!")
        guess = int(input("It's incorrect! Try again: "))
        i += 1
        if guess == the_num:
            print('Congratulations, your guess is correct!')
        elif i == 10 and guess != the_num:    
            print("Your attempts is over!")
            break
       
print(f"The correct number is {the_num}!")


# Codigo do professor:
num = 12
guess = 0
guess_limit=3
guess_number = 0

while guess_number < guess_limit:
    guess = int(input(f'Guess #{guess_number+1} a number 1-20: last guess:{guess} '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    else:
        print(f'No, not {guess}!')
        guess_number += 1
if guess != num:
    print(f'Sorry you lose! It was {num}')