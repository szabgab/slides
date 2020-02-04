import time

def boil_water(sec):
    print(f"Start boiling water for {sec} seconds")
    time.sleep(sec)
    print(f"End boiling water for {sec} seconds")

def washing_machine(sec):
    print(f"Start washing machine")
    time.sleep(sec)
    print(f"End washing machine")

def dryer(sec):
    print(f"Start dryer")
    time.sleep(sec)
    print(f"End dryer")

def dishwasher(sec):
    print(f"Start dishwasher")
    time.sleep(sec)
    print(f"End dishwasher")

def clean_potatoes(pieces):
    print("Start cleaning potatoes")
    for ix in range(pieces):
        print(f"Cleaning potato {ix}")
        time.sleep(0.5)
    print("End cleaning potatoes")

def main():
    dishwasher(3)
    washing_machine(3)
    dryer(3)
    boil_water(4)
    clean_potatoes(14)

start = time.time()
main()
end = time.time()
print(f"Elapsed {end-start}")
