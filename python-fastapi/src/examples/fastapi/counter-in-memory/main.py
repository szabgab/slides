from fastapi import FastAPI

app = FastAPI()

counter = 0

@app.get("/")
async def main():
    global counter
    counter += 1
    return {"cnt": counter}

