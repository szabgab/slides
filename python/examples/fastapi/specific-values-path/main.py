from enum import Enum
from fastapi import FastAPI


class CarTypeName(str, Enum):
    tesla = "Tesla"
    volvo = "Volvo"
    fiat  = "Fiat"



app = FastAPI()


@app.get("/car/{car_type}")
async def get_car(car_type: CarTypeName):
    print(car_type) # CarTypeName.tesla
    if car_type == CarTypeName.tesla:
        print("in a Tesla")
    return {f"car type '{car_type}'"}
