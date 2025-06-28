import random


def number_generator():
    y = [0, 0, 0, 0]

    for i in range(0, 4):
        y[i] = random.randrange(0, 10)
        # print(y)
        if i:
            number += str(y[i])
        else:
            number = str(y[i])
    # print(number)
    return number


def user_input():
    x = input("Type in 4 digits number:")
    if len(x) == 4:
        return x
    else:
        print("wrong input")
        user_input()


def string_compare(x, y):
    r = 0
    q = 0
    for i in range(0, 4):
        if x[i] == y[i]:
            r += 1
            continue
        for j in range(0, 4):
            if x[i] == y[j]:
                if i == j:
                    continue
                else:
                    q += 1
                    break
    return r, q


def print_result(r):
    print("")
    for i in range(0, r[0]):
        print("*", end="")
    for i in range(0, r[1]):
        print("+", end="")
    print("\n")


def main():
    comp = number_generator()
    result = 0
    while True:
        user = user_input()
        result = string_compare(comp, user)
        print_result(result)
        # print(result)
        if result[0] == 4:
            print("Correct!")
            return


main()
