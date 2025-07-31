import time

def sleep(cnt, sec):
    print(f"Start {cnt}")
    time.sleep(sec)
    print(f"End {cnt}")

def main():
    for i in range(4):
        sleep(i, 1)


start = time.monotonic()
main()
end = time.monotonic()
print(f"Elapsed {end-start}")
