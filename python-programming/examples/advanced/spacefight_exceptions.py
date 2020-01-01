import random

class SpaceShipError(Exception):
    def __init__(self, inp):
        self.inp = inp

class NumberTooBigError(SpaceShipError):
    def __str__(self):
        return "Number {} is too big".format(self.inp)

class NumberTooSmallError(SpaceShipError):
    def __str__(self):
        return "Number {} is too small".format(self.inp)


class NotANumberError(SpaceShipError):
    def __str__(self):
        return "Not a Number {}".format(self.inp)


class Game(object):
    def __init__(self):
       self.lower_limit = 0
       self.upper_limit = 200

       self.number = random.randrange(self.lower_limit, self.upper_limit)
       self.is_debug = False
       self.running = True

    def debug(self):
        self.is_debug = not self.is_debug

    def guess(self, num):
        if num == 'd':
            self.debug()
            return

        if self.is_debug:
            print("Hidden number {}. Your guess is {}".format(self.number, num))

        try:
            num =  int(num)
        except Exception:
            raise NotANumberError(num)

        if num > self.upper_limit:
            raise NumberTooBigError(num)

        if num < self.upper_limit:
            raise NumberTooSmallError(num)

        if num < self.number:
            print("Too small")
        elif num > self.number:
            print("Too big")
        else:
            print("Bingo")
            self.running = False


g = Game()
g.guess('d')

try:
    g.guess('z')
except Exception as e:
    print(e)

try:
    g.guess('201')
except Exception as e:
    print(e)

try:
    g.guess('-1')
except Exception as e:
    print(e)



#while g.running:
#    guess = raw_input("Please type in your guess: ")
#    g.guess(int(guess))

