import random

y = random.randrange(1, 21)
x = int(input("Pick an integer between 1-20 and type in your guess:"))

while True:
    if x > y:
        if x > 20:
            print("Out of range!")
            x = int(input("Try again:"))
        else:
            print("Too Big!")
            x = int(input("Guess Again:"))
        continue

    if x < y:
        if x < 1:
            print("Out of range!")
            x = int(input("Try again:"))
        else:
            print("Too Big!")
            x = int(input("Guess Again:"))
        continue
    else:
        print("That is Correct!")
        break
