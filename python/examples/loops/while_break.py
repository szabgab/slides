import random

def random_loop():
    total = 0
    while total < 10000000:
        if total % 17 == 1:
            break

        if total ** 2 % 23 == 7:
            break

        print(total)
        total += random.randrange(20)

        # do the real work here

    print("done")

if __name__ == '__main__':
    random_loop()
