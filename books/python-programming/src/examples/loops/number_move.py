import random

UPPER_LIMIT = 200

hidden = random.randrange(1, UPPER_LIMIT + 1)
debug = False
move = False
while True:
    if debug:
        print(f"Debug: {hidden}")
        print(f"Move: {move}")

    if move:
        mv = random.randrange(-2, 3)
        if 1 <= hidden + mv <= UPPER_LIMIT:
            hidden = hidden + mv

    user_input = input("Please enter your guess [x|s|d|m]: ")
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

    guess = int(user_input)
    if guess == hidden:
        print("Hit!")
        break

    if guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
