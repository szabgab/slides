import random

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

