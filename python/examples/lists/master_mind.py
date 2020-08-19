import random

width = 4
USED  = '_'

hidden = random.sample(range(10), width)
# print(hidden)

while True:
    # print(hidden)

    inp = input("your guess ({} digits):".format(width))
    if inp == 'x':
        print("Bye")
        exit()
    if len(inp) != width:
        print("We need exactly {} characters".format(width))
        continue

    guess = []
    for cr in inp:
        guess.append(int(cr))
    # guess = list(map(int, inp))
    # print(guess)

    if hidden == guess:
        print("Match!")
        break

    my_hidden = hidden[:]
    my_guess  = guess[:]

    result = ''
    for i in range(width):
        if my_hidden[i] == my_guess[i]:
            result  += '*'
            my_hidden[i] = USED
            my_guess[i] = USED
    for i in range(width):
        if my_guess[i] == USED:
            continue
        if my_guess[i] in my_hidden:
            loc = my_hidden.index(my_guess[i])
            my_hidden[loc] = USED
            guess[i] = USED
            result += '+'

    print(''.join(result))
