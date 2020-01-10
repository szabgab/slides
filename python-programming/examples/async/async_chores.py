import time
import asyncio

async def boil_water(sec):
    print(f"Start boiling water for {sec} seconds")
    await asyncio.sleep(sec)
    print(f"End boiling water for {sec} seconds")

async def washing_machine(sec):
    print(f"Start washing machine")
    await asyncio.sleep(sec)
    print(f"End washing machine")

async def dishwasher(sec):
    print(f"Start dishwasher")
    await asyncio.sleep(sec)
    print(f"End dishwasher")


async def clean_potatoes(pieces):
    print("Start cleaning potatoes")
    for ix in range(pieces):
        print(f"Cleaning potato {ix}")
        time.sleep(0.5)
        #await asyncio.sleep(0.0001)
    print("End cleaning potatoes")

async def main():
    await asyncio.gather(dishwasher(3), washing_machine(3), boil_water(4), clean_potatoes(8))

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Elapsed {end-start}")
