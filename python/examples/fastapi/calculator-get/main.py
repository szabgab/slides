from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main(a: int, b: int):
    return {"message": a+b}
