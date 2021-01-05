import time

def say(text, sec):
    time.sleep(sec)
    print(text)

def main():
    start = time.monotonic()
    say("First", 2)
    say("Second", 1)
    end = time.monotonic()
    print(f"Elapsed: {end-start}")

main()

