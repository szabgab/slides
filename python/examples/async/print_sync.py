import time

def say(text, sec):
    time.sleep(sec)
    print(text)

def main():
    say("First", 2)
    say("Second", 1)


main()

