import random

class Game():
    def __init__(self):
        self.hidden = random.randint(1, 200)
        #print(hidden)

    def guess(self, guessed_number):
        if self.hidden == guessed_number:
            return 'match'
        if guessed_number < self.hidden:
            return 'too small'
        return 'too big'

