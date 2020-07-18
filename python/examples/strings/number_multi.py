import random

debug = False
move = False
while True:
    print("\nWelcome to another Number Guessing game")
    hidden = random.randrange(1, 201)
    while True:
        if debug:
            print("Debug: ", hidden)

        if move:
            mv = random.randrange(-2, 3)
            hidden = hidden + mv

        user_input = input("Please enter your guess [x|s|d|m|n]: ")
        print(user_input)

        if user_input == 'x':
            print("Sad to see you leaving early")
            exit()

        if user_input == 's':
            print("The hidden value is ", hidden)
            continue

        if user_input == 'd':
            debug = not debug
            continue

        if user_input == 'm':
            move = not move
            continue

        if user_input == 'n':
            print("Giving up, eh?")
            break

        guess = int(user_input)
        if guess == hidden:
            print("Hit!")
            break

        if guess < hidden:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

