import sys

hidden = 42   # would be random

if sys.version_info.major < 3:
    guess = raw_input('Your guess: ')
else: 
    guess = input('Your guess: ')

if hidden == guess:
    print("Match!")
