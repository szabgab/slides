import random

hidden = random.randrange(1, 201)
debug = False
while True:
    if debug:
        print("Debug: ", hidden)

    user_input = input("Please enter your guess [x|s|d]: ")
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

    guess = int(user_input)
    if guess == hidden:
        print("Hit!")
        break

    if guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
