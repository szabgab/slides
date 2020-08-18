import random

hidden = random.randrange(1, 201)
while True:
    user_input = input("Please enter your guess: ")
    print(user_input)

    guess = int(user_input)
    if guess == hidden:
        print("Hit!")
        break

    if guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
