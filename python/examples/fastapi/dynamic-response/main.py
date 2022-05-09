from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello World at {datetime.datetime.now()}"}

