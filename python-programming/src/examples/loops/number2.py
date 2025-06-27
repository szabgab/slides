import random

hidden = random.randrange(1, 201)
while True:
    user_input = input("Please enter your guess[x]: ")
    print(user_input)

    if user_input == 'x':
        print("Sad to see you leaving early")
        exit()

    guess = int(user_input)
    if guess == hidden:
        print("Hit!")
        break

    if guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
