import random

class Game:
    def __init__(self):
        self.debug = False
        self.move = False

    def check_input(self, user_input):
        print(user_input)
        if user_input == 'x':
            print("Sad to see you leaving early")
            exit()

        if user_input == 's':
            print("The hidden value is ", self.hidden)
            return True

        if user_input == 'd':
            self.debug = not self.debug
            return True

        if user_input == 'm':
            self.move = not self.move
            return True

        if user_input == 'n':
            print("Giving up, eh?")
            return False
        return None


    def run(self):
        while True:
            print("\nWelcome to another Number Guessing game")
            self.hidden = random.randrange(1, 201)
            while True:
                if self.debug:
                    print("Debug: ", self.hidden)

                if self.move:
                    mv = random.randrange(-2, 3)
                    self.hidden += mv

                user_input = input("Please enter your guess [x|s|d|m|n]: ")
                print(user_input)

                handled = self.check_input(user_input)
                if handled:
                    continue
                if handled is not None:
                    break

                guess = int(user_input)
                if guess == self.hidden:
                    print("Hit!")
                    break

                if guess < self.hidden:
                    print("Your guess is too low")
                else:
                    print("Your guess is too high")

def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()