import time


def work(wid, sec):
    start = time.time()
    print(f"Starting {wid} that will take {sec}s")
    time.sleep(sec)
    end = time.time()
    print(f"Finishing {wid} in {end-start}s")

def main():
    work("Blue", 2),
    work("Green", 1)


start = time.time()
main()
end = time.time()
print(f"Elapsed {end-start}")

