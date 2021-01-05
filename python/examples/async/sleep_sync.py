import time


def say(wid, sec):
    start = time.monotonic()
    print(f"Starting {wid} that will take {sec}s")
    time.sleep(sec)
    end = time.monotonic()
    print(f"Finishing {wid} in {end-start}s")

def main():
    start = time.monotonic()
    say("First", 2),
    say("Second", 1)
    end = time.monotonic()
    print(f"Elapsed: {end-start}")


start = time.time()
main()
end = time.time()
print(f"Elapsed {end-start}")

